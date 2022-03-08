#!/usr/bin/env python3
# Create random dna sequences

import random

# Return random CGTA sequences, set minimum = maximum to get a specified length.
def random_length_dnasequence(minimum=300, maximum=15000, actg_distribution=None):
    if (minimum == maximum):
        length = minimum
    else:
        length = random.randint(minimum, maximum)
    if (actg_distribution == None):
        actg_distribution = ''.join(random.choice('cgta') for _x in range(7))

    return ''.join(random.choice(actg_distribution) for _x in range(length))


def random_dnasequence(length, actg_distribution=None):
    return random_length_dnasequence(length, length, actg_distribution)


if __name__ == '__main__':
    # counter
    nstart=1
    # total number of sequences
    nseqs=10000
    # pad zeros to left reference
    padding=len(str(nseqs))
    # min sequence length
    minimo=300
    # max sequence length
    maximo=20000
    # Generate sequences
    while nstart <= nseqs:
        # generate sequence id
        rnd_name = f"rndseq_{str(nstart).zfill(padding)}"
        # generate random sequence
        rnd_seq = random_length_dnasequence(minimum=minimo,maximum=maximo)
        # print to stdout
        print(f'>{rnd_name}\n{rnd_seq}')
        # increase counter
        nstart+=1
    