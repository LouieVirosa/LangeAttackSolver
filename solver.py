#!/usr/bin/env python3
'''
Automated solver for the geocaching puzzle at: https://www.geocaching.com/geocache/GCH2GC_max-lange-attack
'''
import itertools

langemoves = ["P-K4", "P-K4", "N-KB3", "N-QB3", "B-B4", "N-B3", "P-Q4", "PxP", "O-O", "P-Q3", "NxP", "B-K2", "N-QB3", "O-O", "P-KR3", "R-K1", "R-K1", "N-Q2", "BxP", "KxB", "N-K6", "KxN", "Q-Q5", "K-B3", "Q-KB5"]

# The following globals allow for us to manipulate the set of symbols used in the 25-move chess game above
digichars = [str(i) for i in range(10)] # Digits 0-9 as chars so we can ignore them
langeset = {i for ele in langemoves for i in ele if i not in digichars} # set of unique chars from langemoves
langelist = list(langeset) # list of unique chars from langemoves, as they are mutable
langelist.append('H') # 'H' is in the solution, but not the 25 moves. Adding it manually.

def map_symbols(string, curmap):
    """
    Returns an int that is the representation of a string such as "PxK4", using a passed in map
    """
    l1 = list(map(lambda x:curmap[langelist.index(x)] if x not in digichars else int(x), string))
    return int(''.join(map(str,l1)))


def test_solution(curmap):
    '''
    Maps all 25 moves to integer representations, adds them up, and compares to the solution string "BOOHOO"
    given a map.
    curmap: Currrent mapping of langelist of unique symbols to digits. I probably should have done this
        as a dict, but it is a list, and should be of the form [0,1,2,3,4,5,6,7,8,9] or similar.
    '''
    langesum = sum(list(map(lambda x:map_symbols(x, curmap), langemoves)))
    solsum = map_symbols("BOOHOO", curmap)
    if langesum == solsum:
        print("FOUND SOLUTION!")
        print(f"LangeList: {langelist}")
        print(f"Mapping: {curmap}")
        return True
    return False


if __name__ == "__main__":
    '''
    Iterates through all permutations of [0,1,2,3,4,5,6,7,8,9] and checks for solutions that sum to 'BOOHOO'.
    There are 3 solutions, but 2 are disallows because they create integers that start with 0. Manually check
    for these and translate the final clue into a UTM grid coord using the printed mappings.
    '''
    print("Starting brute force for max lange attack...")
    for i in itertools.permutations([0,1,2,3,4,5,6,7,8,9]):
        if test_solution(i):
            # Test to make sure none of the 25 moves starts with 0
            soln_dict = {langelist[y]:i[y] for y in range(len(i))}
            zero_char = next((char for char, val in soln_dict.items() if val == 0), None)
            if any(l.startswith(zero_char) for l in langemoves):
                print(f"Found FALSE Solution: {soln_dict}\n\n")
            else: 
                print(f"**** FOUND TRUE SOLUTION: {soln_dict} ****")
                final_coords = str(map_symbols('QN-B-NPRHRBQN--O', i))
                coords_str = f"{final_coords[:2]}S {final_coords[2:9]} {final_coords[9:]}"
                print(f"Final Coords: {coords_str}\n\n")
                
    print("Done!")
