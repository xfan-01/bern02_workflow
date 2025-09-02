#Running exercise 1
#Author: Xing Fan

#add some head block
#%%
import sys
fasta_file = sys.argv[1]
blastx_file = sys.argv[2]
output_file = sys.argv[3]

#%% create a dictionary that corresponds gene IDs to protein descriptions

#before running the script, make sure you the blastx file where gene id in the first column, protein description in the 10th column

protein_dict = {}
with open(blastx_file, 'r') as file:  # open the blastx file
    for line in file:
        if line.startswith('#'):  # skip lines starting with #
            continue
        line = line.rstrip()
        fields = line.split('\t')  # split the line by tab
        gene_id = fields[0]  # get the gene ID
        protein_description = fields[9]  # get the protein description
        if protein_description != 'null':  
            protein_dict[gene_id] = protein_description # add the gene ID and protein description to the dictionary

#%% read the fasta file, add protein description and create an output file

with open(fasta_file, 'r') as file, open(output_file, 'w') as output:  # open fasta and output files
    for line in file:
        line = line.rstrip()
        if line.startswith('>'):
            header = line[1:]  # get the header without '>'
            fields = header.split('\t')  # split to extract gene ID
            gene_id = fields[0]
            if gene_id in protein_dict:
                output.write('>' + header + '\t' + 'protein='+ protein_dict[gene_id] + '\n')   # write the header with protein description
                # make sure the sequence only has one line and immediately follows the header
                output.write(next(file))   #write the sequence line
                
#%%



