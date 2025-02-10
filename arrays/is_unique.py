# IS UNIQUE # page # 90
# Implement an algorithm to determine if a string has all unique characters.
# hints: #44, #117, #132

def is_unique(string: str) -> bool:
    """
    A space efficient Python3 program to check if all characters of string are unique
    Assumptions:
        (1) str contains only characters from 'a' to 'z' 
        (2) integers are stored using 32 bits
    src: https://www.geeksforgeeks.org/efficiently-check-string-duplicates-without-using-additional-data-structure/
    pseudo code:
    1. get the ascii value for each element in the array
    2. set the ascii value as a bit in the `checker` variable: `checker |= (1 << val)`
    3. before setting the above bit, first check if it is already set, if it is then there is a duplicate
    """
    # An integer to store presence/absence of 26 characters using its 32 bits
    checker = 0
    length = len(string)
    for i in range(length):
        val = ord(string[i]) - ord('a')

        # If bit corresponding to current character is already set
        if ( checker & (1 << val) ) > 0:
            return False

        # set bit in checker 
        checker |= (1 << val)
    return True

def is_unique_brute_force(string: str) -> bool:
    """
    1. compare each element every other element in the array; very inefficient.
    """
    length = len(string)
    for i in range(length):
        for j in range(i+1, length):
            if string[i] == string[j]:
                return False
    return True

def is_unique_using_list(string: str) -> bool:
    """
    1. sort the string array
    2. if the two adjacent elements are the same, then there is a duplicate
    """
    mylist = list(string)
    mylist.sort()
    for i in range(len(mylist)-1):
        if mylist[i] == mylist[i+1]:
            return False
    return True

if __name__ == "__main__":
    print(is_unique('foo'))
    print(is_unique('for'))

    print(is_unique_using_list('foo'))
    print(is_unique_using_list('for'))

    print(is_unique_brute_force('foo'))
    print(is_unique_brute_force('for'))
