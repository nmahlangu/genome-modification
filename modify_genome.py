import sys

# generates the reverse complement of a codon
def generate_reverse_complement(codon):
	new_codon = ""
	for l in reversed(codon):
		new_codon += "T" if l == "A" else "A" if l == "T" else "C" if l == "G" else "G"
	return new_codon

# `replacement_codon` will replace `bad_codon` (for normal genes)
# `rev_comp_replacement_codon` will replace `rev_comp_bad_codon` (for complement genes)
bad_codon = "TTG"
rev_comp_bad_codon = generate_reverse_complement(bad_codon)
replacement_codon = "CTA"
rev_comp_replacement_codon = generate_reverse_complement(replacement_codon)

# input paths and files
genome_path = "./genome.txt"
genome_file = open(genome_path)
genome_bank_path = "./genome_bank.txt"
genome_bank_file = open(genome_bank_path)

# log file
log_path = "./log.txt"
log = open(log_path, "w")

# output file
output_path = "./modified_genome.txt"
output = open(output_path, "w")

# get all of the lines in the genome
gene_lines  = []
for line in genome_file:
	gene_lines.append(line.replace("\n",""))
gene_lines = gene_lines[1:]

# get all of the lines in the genome bank
bank_lines = []
for line in genome_bank_file:
	bank_lines.append(line)

# get all of the start/stop points
bounds = []
for line in bank_lines:
	if "   gene   " in line:
		if "complement" in line:
			s = line.split(" ")[-1].split(".")
			start = int(s[0].replace("complement(","")) - 1
			stop = int(s[-1].replace("\n","").replace(")","")) - 1
			bounds.append((start,stop,"complement"))
		else:
			s = line.split(" ")[-1].split(".")	
			start = int(s[0]) - 1
			stop = int(s[-1].replace("\n", "")) - 1
			bounds.append((start,stop,"normal"))

# generate entire genome
genome = "".join(gene_lines)

# create new genome 
# glb: gene lower bound 
# gub: gene upper bound
# bt: bound type (either "normal" or "complement")
count = 1
for (glb,gub,bt) in bounds:
	status = "\rModifying gene %d of %d" % (count, len(bounds))
	count += 1
	sys.stdout.write(status)
	sys.stdout.flush()
	log.write("[Gene Bounds]: (%d,%d)\n\n" % (glb+1,gub+1))  # log
	substring = genome[glb:gub + 1]
	codons = [substring[i:i+3] for i in range(0,len(substring),3)]
	log_codons = [s.replace(bad_codon, "--(("+ bad_codon + "))--") for s in codons] if bt == "normal" else [s.replace(rev_comp_bad_codon, "--((" + rev_comp_bad_codon + "))--") for s in codons] # log
	log.write("[Original Gene]: " + "".join(log_codons) + "\n\n")  # log
	if bt == "normal":
		tmp = codons # log
		codons = [s.replace(bad_codon,replacement_codon) for s in codons]
		log_codons = [s.replace(bad_codon, "--((" + replacement_codon + "))--") for s in tmp]  # log
	elif bt == "complement":
		tmp = codons # log
		codons = [s.replace(rev_comp_bad_codon,rev_comp_replacement_codon) for s in codons]
		log_codons = [s.replace(rev_comp_bad_codon, "--((" + rev_comp_replacement_codon + "))--") for s in tmp]  # log
	substring = "".join(codons)
	genome = genome[:glb] + substring + genome[gub + 1:]
	log.write("[Modified Gene]: " + "".join(log_codons) + "\n")	 # log
	log.write("**********************************************\n")  # log

# write modified genome to output
genome_lines = [genome[i:i+70] for i in range(0,len(genome),70)]
for line in genome_lines:
	output.write(line + "\n")

# clean up
print "\nDone!"
genome_file.close()
genome_bank_file.close()
log.close()
output.close()
