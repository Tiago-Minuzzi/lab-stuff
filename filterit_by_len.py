#!/usr/bin/env python3

import os
import sys
from Bio import SeqIO

SCRIPT = sys.argv[0]
CWD = os.getcwd()

class Inspetor:
    def __init__(self,arquivo):
        self.arquivo = arquivo
        self.diretorio = os.path.dirname(self.arquivo)
        self.caminho = os.path.abspath(self.diretorio)
        self.nome = os.path.basename(self.arquivo)
        self.novo = f'filtered_{self.nome}'
        self.saida = os.path.join(self.caminho, self.novo)

        with open(self.arquivo) as arq_in:
            self.palavras = []
            for record in SeqIO.parse(arq_in, 'fasta'):
                 
                self.palavras.append(len(record.seq))
            self.palavras = set(self.palavras)
            self.def_menor = min(self.palavras)
            self.def_maior = max(self.palavras)


if __name__ == '__main__':
    try:
        ARQUIVO = sys.argv[1]
        valor = Inspetor(ARQUIVO)
        print(f'''
# Select Sequences with desired lengths.
# Let it empty for default values.
# Defaults: min = {valor.def_menor}, max = {valor.def_maior}.
                ''')
        with open(valor.arquivo) as fasin, open(valor.saida, 'w') as fasout:
            menor = int(input('- Enter min length: ') or valor.def_menor)
            maior = int(input('- Enter max length: ') or valor.def_maior)
            for record in SeqIO.parse(fasin, 'fasta'):
                seq_len = len(record.seq)
                if menor <= seq_len <= maior:
                    SeqIO.write(record, fasout, 'fasta-2line')
            if valor.caminho == CWD:
                print(f'Saved as {valor.novo}.')
            else:
                print(f'Saved in {valor.caminho} as {valor.novo}.')
    except IndexError:
        print('# No file entered.\n# Please enter file name/location.')
        print('# Run:')
        print(f'python3 {SCRIPT} file.fasta')
    except FileNotFoundError:
        print(f"File '{ARQUIVO}' not found.")
    except KeyboardInterrupt:
        print('\n\nEnded by user.')
        print('Bye, bye.')
