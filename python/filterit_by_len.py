#!/usr/bin/env python3

import os
import sys
from Bio import SeqIO
# Vars for error handling and comparison
SCRIPT = sys.argv[0]
CWD = os.getcwd()
# Class to get file info and create default values
class Inspetor:
    def __init__(self,arquivo):
        # Get file info
        self.arquivo = arquivo
        self.diretorio = os.path.dirname(self.arquivo)
        self.caminho = os.path.abspath(self.diretorio)
        self.nome = os.path.basename(self.arquivo)
        self.novo = f'filtered_{self.nome}'
        # Create default values
        with open(self.arquivo) as arq_in:
            self.palavras = []
            for record in SeqIO.parse(arq_in, 'fasta'):
                # Append sequence lengths to list 
                self.palavras.append(len(record.seq))
            self.palavras = set(self.palavras)
            self.def_menor = min(self.palavras)
            self.def_maior = max(self.palavras)


if __name__ == '__main__':
    try:
        # Get input from prompt
        ARQUIVO = sys.argv[1]
        # Initialize class
        valor = Inspetor(ARQUIVO)
        print(f'''
# Select Sequences with desired lengths.
# Let it empty for default values.
# Defaults: min = {valor.def_menor}, max = {valor.def_maior}.
# Default name: {valor.novo}
                ''')
        with open(valor.arquivo) as fasin:
            menor = int(input('- Enter min length: ') or valor.def_menor) # set default min length
            maior = int(input('- Enter max length: ') or valor.def_maior) # set default max length
            novo = input('- Enter output file name: ') or valor.novo # set default file name
            fasout = os.path.join(valor.caminho, novo)
            with open(fasout, 'w') as fasout:
                for record in SeqIO.parse(fasin, 'fasta'):
                    seq_len = len(record.seq)
                    if menor <= seq_len <= maior:
                        SeqIO.write(record, fasout, 'fasta-2line')
            if valor.caminho == CWD:
                print(f'Saved as {novo}.')
            else:
                print(f'Saved in {valor.caminho} as {novo}.')
    except IndexError:
        print('# No file entered.\n# Please enter file name/location.')
        print('# Run:')
        print(f'python3 {SCRIPT} file.fasta')
    except FileNotFoundError:
        print(f"File '{ARQUIVO}' not found.")
    except KeyboardInterrupt:
        print('\n\nEnded by user.')
        print('Bye, bye.')
