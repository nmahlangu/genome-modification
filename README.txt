Files
- modify_genome.py
- genome.txt
- genome_bank.txt
- modified_genome.txt (will be created)
- log.txt (will be created)

Instructions
- Put all 3 files (modify_genome.py, genome.txt, and genome_bank.txt) into
  one directory (e.g. ~/Desktop). Then navigate to that directory using 
  terminal and once inside, type "python modify_genome.py". This will create
  log.txt and modified_genome.txt in the same directory, the latter of which
  will contain the modified genome.

Notes
- To change what codon should be replaced, edit the variable `bad_codon`
  on line 4 of modify_genome.py.
- To change what codon should be replacing `bad_codon`, edit the variable
  `replacement_codon` on line 5 of modify_genome.py.
- log.txt is a log of every single change that is made in a gene (it's
  useful!!!!). In each section separated by asterisks, the bounds of the
  gene are shown, as well as the original gene and the modified gene.
  Note that all of the `bad_codons` are demarked with "--(XXX)--" in the 
  original gene, and all of the `replacement_codons` are demarked with
  "--(XXX)--". Essentially, it is very clear which genes were replaced.
- modified_genome.txt contains the modified genome in the same format as
  it was given in genome.txt (70 characters, either A,C,G, or T) per line.
- Since a genome is not zero-indexed, all "bounds" in the code will be 1
  less than they actually are to account for 0-indexing of arrays and such
  (e.g. if a particular gene's bounds are (190,255), it will instead be 
  represented as (189, 254)). However, log.txt will display what the actual
  bounds are using 1-indexing.  

Dependencies
- modify_genome.py assumes that the first line of genome.txt is useless
  information
