"""
Implement a method perform basic string compression using the counts of repeated characters. For example,
the string aabcccccaaa wold become a2b1c5a3. If the "compressed" string would not become smaller than the
original string, your method should return the original string. You can assume the string has only uppercase
and lowercase letters (a-z).
Hints: #92, #110
"""

class Solution:
    def compress(self, input: str) -> str:
        compressed_string_array = []
        repeat_count = 1
        compressed_string_array.append(input[0])
        for i in range(1, len(input)):
            if input[i-1] == input[i]:
                repeat_count += 1
            else:
                compressed_string_array.append(str(repeat_count))
                compressed_string_array.append(input[i])
                repeat_count = 1
        compressed_string_array.append(str(repeat_count))
        if len(input) <= len(compressed_string_array):
            return input
        return ''.join(compressed_string_array)

if __name__ == '__main__':
    solution = Solution()
    # input = 'aabcccccaaa'
    input = 'aaaaaaaaaghhh'
    print(f'input={input}, compressed_input={solution.compress(input)}')
