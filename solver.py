#!/usr/bin/env python3
'''
Automated solver for the geocaching puzzle at: https://www.geocaching.com/geocache/GCH2GC_max-lange-attack
'''
import itertools

langemoves = ["P-K4", "P-K4", "N-KB3", "N-QB3", "B-B4", "N-B3", "P-Q4", "PxP", "O-O", "P-Q3", "NxP", "B-K2", "N-QB3", "O-O", "P-KR3", "R-K1", "R-K1", "N-Q2", "BxP", "KxB", "N-K6", "KxN", "Q-Q5", "K-B3", "Q-KB5"]

digichars = [str(i) for i in range(10)]
langeset = {i for ele in langemoves for i in ele if i not in digichars}
langelist = list(langeset)
langelist.append('H')

def map_symbols(string, curmap):
    """
    Returns an int that is the representation of a string such as "PxK4", using a passed in map
    """

    l1 = list(map(lambda x:curmap[langelist.index(x)] if x not in digichars else int(x), string))
    return int(''.join(map(str,l1)))

def test_solution(curmap):
    langesum = sum(list(map(lambda x:map_symbols(x, curmap), langemoves)))
    solsum = map_symbols("BOOHOO", curmap)
    if langesum == solsum:
        print("FOUND SOLUTION!")
        print(f"LangeList: {langelist}")
        print(f"Mapping: {curmap}")
        return True
    return False


if __name__ == "__main__":
    print("Starting brute force for max lange attack...")
    for i in itertools.permutations([0,1,2,3,4,5,6,7,8,9]):
        test_solution(i)
    print("Done!")
