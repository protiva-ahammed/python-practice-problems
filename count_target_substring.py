from itertools import product

"""
    Brute force: generate every possible string, check if subPattern is in it.
    Simple, but O(alphabet_size ^ length) time -> only works for small inputs.

    product("AEIOKU", repeat=5) means:
    for a in "AEIOKU":
    for b in "AEIOKU":
        for c in "AEIOKU":
            for d in "AEIOKU":
                for e in "AEIOKU":
                    combo = (a, b, c, d, e)
                    # do something with combo
"""

def count_strings_with_target_pattern(alphabet, length, subPattern):
    count = 0
    # Generate every possible string of given length using the alphabet
    for i in product(alphabet,repeat=length):
        s=''.join(i)
        if subPattern in s:
            count+=1

    return count




if __name__ == "__main__":
    alphabet = "AEIOKU"
    length = 5
    subPattern='OK'
 
    result = count_strings_with_target_pattern(alphabet, length, subPattern)
    print(f"Strings containing subPattern : {result}")