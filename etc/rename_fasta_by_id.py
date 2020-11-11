#!/usr/bin/env python3
import os
import pathlib

# Set directory and file extension
folder = '/home/labdros/labdros4/tiago_minuzzi/wolbachia/ena_wolb_wgs'
fext = '.fasta'
# Iterate over files in directory
for path in pathlib.Path(folder).iterdir():
	if path.suffix == fext:
		with open(path,'r') as f:
			# Get new name from genome id in fasta id
			fline = f.readline().strip()
			fline = fline.split(' ')[5]
		file_name = str(path).split('/')[-1]
		new_file = f'{fline}_{file_name}'
		# Rename files
		os.rename(path, new_file)