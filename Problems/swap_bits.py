'''
Given a number and two indexes i,j, swap the bits at the positions i,j
'''

def swap_bits(nr, i, j):
    nri = ((1 << i) & nr) >> i
    nrj = ((1 << j) & nr) >> j

    if nri & 1 != nrj & 1:
        or_shift, and_shift = (i, j) if not nri & 1 else (j, i)
        nr = (1 << or_shift) | nr
        nr = (~(1 << and_shift)) & nr
    
    print(nr)


def swap_bits_2(nr, i, j):
    return nr ^ ((1 << i) | (1 << j)) if (nr >> i) & 1 != (nr >> j) & 1 else nr
    

print(swap_bits_2(45, 4, 1))