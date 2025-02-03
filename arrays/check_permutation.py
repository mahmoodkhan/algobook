from typing import Dict
from collections import defaultdict

# Check Permutation, page # 90
# given two strings, write a method to decide if one is a permutation of the other
# hint: #1, #84, #122, #131

def is_permutation(str1: str, str2: str) -> bool:
    """
    A space efficient Python3 program to check if one string is a permutation of the other string
    Assumptions:
        (1) str contains only characters from 'a' to 'z' 
        (2) integers are stored using 32 bits
    """
    len1 = len(str1)
    len2 = len(str2)
    if len1 != len2:
        return False

    # An integer to store presence/absence of 26 characters using its 32 bits
    checker = 0

    for i in range(len1):
        val = ord(str1[i]) - ord('a')
        # set bit in checker
        checker |= (1 << val)

    for j in range(len2):
        val = ord(str2[j]) - ord('a')
        # If bit corresponding to current character is NOT set then the 2nd string is not a permutation
        if (checker & (1 << val)) <= 0:
            return False
    return True


def is_permutation2(str1: str, str2: str) -> bool:
    if len(str1) != len(str2):
        return False

    d: Dict = defaultdict(int)
    for c in str1:
        d[c] += 1
    for c in str2:
        d[c] -= 1

    # return True if there are no values
    return not any(d.values())

def is_permutation3(str1: str, str2: str) -> bool:
    if len(str1) != len(str2):
        return False
    s1_sorted = sorted(str1)
    s2_sorted = sorted(str2)
    if s1_sorted != s2_sorted:
        return False
    return True



if __name__ == "__main__":
    print(is_permutation('foo', 'oof'))
    print(is_permutation('foo', 'ofo'))
    print(is_permutation('foo', 'ofo'))

    print(is_permutation2('foo', 'oof'))
    print(is_permutation2('fo1', 'o1f'))

    print(is_permutation3('foo', 'oof'))
    print(is_permutation3('fo1', 'o1f'))
