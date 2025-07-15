from ase.io import read, write

# Filepath to the QE SCF output file
qe_output_file = "/Users/seyeong/Desktop/UNIST/25winter/HandsOn/lab7/pt_scf.out"

# Read the QE output file using ASE
structure = read(qe_output_file)

# Write the structure to a POSCAR file
poscar_file = "/Users/seyeong/Desktop/UNIST/25winter/HandsOn/lab7/pt_structure.POSCAR"
write(poscar_file, structure, format='vasp')

print("POSCAR file has been generated.")