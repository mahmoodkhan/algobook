# URLify
# Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string.
# EXAMPLE:
# Input:  "Mr John Smith    ", 13
# Output: "Mr%20John%20Smith"

from typing import List

def urlify(string: str) -> str:
    """
    pseudo code:
    1. loop over characters from left to right
    2. if it is a space
    2a. shift the array by two characters to the right
    2b. fill the 3 spaces with '%', '2', and '0'
    3. if it is not a space, go to the next character
    4. return the list of characters as a string
    """
    chars = list(string)
    n = 0
    while n < len(chars):
        if chars[n] == " ":
            make_room(n, chars) 
            chars[n] = '%'
            chars[n+1] = '2'
            chars[n+2] = '0'
            n += 2
        else:
            n += 1
    return str(chars)

def make_room(l_index: int, chars: List[chr]) -> None:
    """
    assumption:
        there is always empty spaces at the end of the array.
    pseudo code:
    l_index: the left index at which an empty space was encountered
    chars: the array whose elements located after l_index are to be shifted two spaces to the right.
    1. find the index of the first non-whitespace character going from right to left.
    2. shift each character by two places
    """
    size = len(chars) - 1
    first_non_whitespace = False
    while size > l_index:
        if chars[size] == ' ' and first_non_whitespace is False:
            size -= 1
            continue
        first_non_whitespace = True
        chars[size+2] = chars[size]
        chars[size] = ' '
        size -= 1



def helper_shift_array(chars: List[chr]) -> List[chr]:
    """
    This is just an extra method I wrote for fun; not related to the problem above.
    shifts all characters non-whitespace characters to the end of the array
    pseudo code:
    current_index: starts from the end of the array and goes towards left
    r: starts at the right most index of the array
    1. start at the end of the array and go left until the FIRST WHITESPACE is found
    2. now keep moving the `current_index` left until the first non-whitespace character is found
    3. start moving non-whitespace chars with whitespace chars to the right
    """
    current_index: int = len(chars) - 1
    r: int = current_index
    first_whitespace_found: bool = False
    while current_index >= 0:
        if chars[current_index] == ' ' and first_whitespace_found is False:
            first_whitespace_found = True
            r = current_index
        if first_whitespace_found is True and chars[current_index] != ' ':
            chars[r] = chars[current_index]
            chars[current_index] = ' '
            r -= 1
        current_index -= 1
    print(chars)


if __name__ == '__main__':
    # urlify = Urlify()
    # chars = ['f', ' ', 'o']
    # urlify.helper_shift_array(chars)
    chars2 = [' ', 'f', ' ', 'o', 'q', ' ', ' ', 'i', ' ']
    helper_shift_array(chars2)
    # chars3 = ['M', 'r', ' ', 'J', 'o', 'h', 'n', ' ', 'S', 'm', 'i', 't', 'h', ' ', ' ', ' ', ' ']
    # urlify.helper_shift_array(chars3)

    result = urlify('Mr John Smith    ')
    print(result)
