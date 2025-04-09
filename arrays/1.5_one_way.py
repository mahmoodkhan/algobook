"""
There are three types of edits that can be performed on strings: insert a character, remove a character, or a replace
a character. Given two strings, write a function to check if they are one edit (or zero edit) away.

Example:
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false
Hints: #23, #97, #130
"""
class Solution:
    """
    The solution assumes str1 and str2 inputs to consist of only lowercase english letters from 'a' to 'z'
    1. If the length of the two strings is more than 1 then it is more than one edit away so return False
    2. Set the bit in `mask` to 1 for each character in str1
    3. Each character in str2 should have the same bit set in `mask` if there are two such bits that evaluate to zero
    .. then it is more than one edit away.
    """
    def is_one_edit_away(self, str1: str, str2: str) -> bool:
        # if one string is bigger/smaller than the other string by more than 1 character then it is NOT one edit away
        chars_diff_count: int = abs(len(str1) - len(str2))
        if chars_diff_count > 1:
            return False

        mask: int = 0
        for i in range(0, len(str1)):
            ascii_value = ord('z') - ord(str1[i])
            mask |= (1 << ascii_value)

        for c in str2:
            ascii_value = ord('z') - ord(c)
            if mask & (1 << ascii_value) == 0:
                chars_diff_count+= 1
            if chars_diff_count > 1:
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    print(f'"pale", "ple" -> {s.is_one_edit_away('pale', 'ple')}')
    print(f'"pales", "pale" -> {s.is_one_edit_away('pales', 'pale')}')
    print(f'"pale", "bale" -> {s.is_one_edit_away('pale', 'bale')}')
    print(f'"pale", "bake" -> {s.is_one_edit_away('pale', 'bake')}')
