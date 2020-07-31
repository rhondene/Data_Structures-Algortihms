""" Problem: there are n people standing in a circle, of which you are one. 
Someone outside the circle goes around clockwise and repeatedly eliminates every other person in the circle, until one person — the winner — remains.
Where should you stand so you become the winner?"""

import numpy as np 

def josephus_solution(n):
    
    ##rule 1: winning position is 1 if n is an exact power of 2    
    if isinstance(np.log2(n),int): 
        return 1
    
    #rule2:  the winning position is the twice the difference n and 2^x plus  1,  
    #   where 2^x is the power of 2 that is closest to n but less than n. if n=7, the 2^x should be 2^2 or 4
    #    note that rule 2 takes care arguments rule 1
    
    #find the round-down exponent that relates n to 2 
    x = int(np.log2(n))  #int will round down a float if n is not a power of 2
    power2 = 2**x
    return (n-power2)*2+1
