"""
Palindrome Permutation
Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a 
word or phrase that is the same forward and backwards. A permutation is a re-arrangement of letters.

The palindrome does not need to be limited to dictionary words. You can ignore casing and non-letter
characters.

Example:
input: "tact coa"
output: True (permutations: "taco cat", "atco cta", etc)
"""

from typing import List
TEXT = 'tact coa'

class Solution1:
    def _build_frequency_array(self, text: str) -> List:
        frequency_array = [0] * 26
        for c in text:
            ascii_value = ord('z') - ord(c)
            if ascii_value < 26:
                frequency_array[ascii_value] += 1
        return frequency_array


    def is_palindrome(self, text: str) -> bool:
        freq_array = self._build_frequency_array(text)
        odd_count = 0
        for num in freq_array:
            if num % 2 > 0:
                odd_count += 1
            if odd_count > 1:
                return False
        return True

    def run(self, text: str = None):
        if text is None:
            text = TEXT
        result = self.is_palindrome(text)
        print(f'Solution1: is "{text}" a palindrome permutation: {result}')

class Solution2:
    """
    This solution only considers lower case english letters; ignoring everything else.

    All I need to know is whether the count of each letter is even or odd. I use a single integer (as a bit vector).
    1. Map each letter to the ascii value between 0 and 25
    2. Flip the integer bit at that ascii value. (If there are two `a` letters then the 0th bit will first flip to 1
    .. and then back to 0)
    3. At the end of the loop, I check that at most one bit is set to 1 in the integer. For a string to be a palindrome
    .. there has to be at most one odd letter or no odd letters at all. So suppose there is one odd letter and the 
    .. integer (used bit vector) will look something like 00010000 so I subtract 1 from it, we'll get 00001111. Note
    .. that there is no overlap so if I don an & (bitwise AND) operation we'll get:
    .. 00010000 & 00001111 = 0, which means there is one odd letter and thus the string is a palindrome.
    .. 
    .. Now let's suppose there is no odd letter so the integer (bit vector) will look like 00000000 and if I subtract
    .. 1 from it, it will look like:
    .. 00000000 - 1 = -1, it means there is no odd letters and the string is a palindrome
    ..
    .. Finally if there is more than one odd letters then the integer (bit vector) might look like 00001011 and if  I
    .. subtract 1 from it, it will look like:
    .. 00001011 - 1 = 00001010
    .. 00001011 & 00001010 =  00001010, this value is greater than one meaning there is more than odd letter and thus 
    .. not a palindrome text.
    """
    def is_palindrome(self, text: str) -> bool:
        mask: int = 0
        for c in text:
            ascii_value = ord('z') - ord(c)
            if ascii_value < 0 or ascii_value > 26:
                continue
            mask ^= (1 << ascii_value)  # flip the bit
        opposite = mask - 1
        if (mask & opposite) > 1:
            return False
        return True

    def run(self, text: str = None):
        if text is None:
            text = TEXT
        result = self.is_palindrome(text)
        print(f'Solution2: is "{text}" a palindrome permutation: {result}')


if __name__ == '__main__':
    text = 'tact coa'
    Solution1().run(text)
    Solution2().run(text)
