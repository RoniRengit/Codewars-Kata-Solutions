"""
Description:

Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells
and carries the "instructions" for the development and functioning of living
organisms.

If you want to know more http://en.wikipedia.org/wiki/DNA

In DNA strings, symbols "A" and "T" are complements of each other,
as "C" and "G". You have function with one side of the DNA
(string, except for Haskell); you need to get the other complementary side.
DNA strand is never empty or there is no DNA at all (again, except for Haskell).

Author: Roni Rengit
"""

def DNA_strand(dna):
    """Find the completementary DNA strand"""
    
    symbols = {'A':'T', 'C':'G', 'T':'A', 'G':'C'}
    comp = ''
    for nucleobases in dna:
        comp += symbols[nucleobases]
    return comp

# Test Cases
DNA_strand ("ATTGC") # return "TAACG"

DNA_strand ("GTAT") # return "CATA"
