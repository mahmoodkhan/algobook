"""
Given an image represented by an N x N matrix, where each pixel in the image is represented by an integer,
write a method to rotate the image by 90 degrees. Can you do this in place?
Hints: #92, #110
"""

from typing import List
class Solution:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.size = len(self.matrix)

    def print_matrix(self):
        for row in range(self.size):
            for col in range(self.size):
                print(f'{self.matrix[row][col]:02d}', end=' ')
            print('')

    def rotate_matrix_counter_clockwise(self):
        matrix2 = [[0] * self.size] * self.size
        matrix2 = [[0 for x in range(self.size)] for y in range(self.size)]
        for row in range(self.size):
            for col in range(self.size):
                m2r = self.size - col - 1
                matrix2[m2r][row] = self.matrix[row][col]
        self.matrix = matrix2

    def rotate_matrix_clockwise(self):
        """

        The first layer is the outer layer consisting of:
        1   2   3   4   5
        6               10
        11              15
        16              20
        21  22  23  24  25

        For the first layer shown above:
        . layer = first = 0
        . last = 4 because 5 - 1 - 0 = 4
        . offset = 0 - 0 = 0
        01  02  03  04  05             21 16 11 06 01 
        06  07  08  09  10             22 17 12 07 02 
        11  12  13  14  15      =>     23 18 13 08 03 
        16  17  18  19  20             24 19 14 09 04 
        21  22  23  24  25             25 20 15 10 05 

        layers = 2
        layer | first | last | i | offset
        0     | 0     | 4    | 0 | 0
        0     | 0     | 4    | 1 | 1
        0     | 0     | 4    | 2 | 2
        0     | 0     | 4    | 3 | 3
        1     | 1     | 3    | 1 | 0
        1     | 1     | 3    | 2 | 1
        """
        layers = self.size // 2
        for layer in range(layers):
            for i in range(layer, self.size - 1 - layer):
                top = self.matrix[layer][i]
                # top <- left
                left = self.matrix[self.size - 1 - i][layer]
                self.matrix[layer][i] = left 

                # left <- bottom
                bottom = self.matrix[self.size - 1 - layer][self.size - 1 - i]
                self.matrix[self.size - 1 - i][layer] = bottom

                # bottom <- right
                right = self.matrix[i][self.size - 1 - layer]
                self.matrix[self.size - 1 - layer][self.size - 1 - i] = right

                # right <- top
                self.matrix[i][self.size - 1 - layer] = top


        # layers = self.size // 2
        # for layer in range(layers):
        #     first = layer
        #     last = self.size - 1 - layer
        #     for i in range(first, last):
        #         offset = i - first
        #         # print(f'{layer} | {first} | {last} | {i} | {offset}')
        #         top = self.matrix[first][i]
        #         # top <- left
        #         self.matrix[first][i] = self.matrix[last-offset][first]

        #         # left <- bottom
        #         self.matrix[last-offset][first] = self.matrix[last][last-offset]

        #         # bottom <- right
        #         self.matrix[last][last - offset] = self.matrix[i][last]

        #         # right <- top
        #         self.matrix[i][last] = top



if __name__ == '__main__':
    matrix_90_l = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    matrix_90_r = [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3],
    ]

    matrix = [
        [1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25],
    ]
    s = Solution(matrix)
    s.print_matrix()
    # s.rotate_matrix_counter_clockwise()
    s.rotate_matrix_clockwise()
    print('\n')
    s.print_matrix()
