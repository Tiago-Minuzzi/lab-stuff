#!/usr/bin/env python3
import os
import pathlib

# Set directory and file extension
folder = '/home/tiago/Desktop/teste'
fext = '.txt'
new_name = '_mitgen.fasta'
# Iterate over files in directory
for path in pathlib.Path(folder).iterdir():
	if path.suffix == fext:
		with open(path,'r') as f:
			# Get new name from genome id in fasta id
			fline = f.readline().strip()
			fline = fline.split('.')[0]
			_, fid = fline.split('|')
			new_file = f'{fid}{new_name}'
		# Rename files
		os.rename(path, new_file)