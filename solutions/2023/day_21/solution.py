# puzzle prompt: https://adventofcode.com/2023/day/21

from ...base import StrSplitSolution, answer
from collections import deque
import numpy as np
from math import ceil

class Solution(StrSplitSolution):
    _year = 2023
    _day = 21

    DIRECTIONS = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    ROCK = "#"

    def expand_matrix(self, matrix, factor):
        return [
            [
                matrix[i % len(matrix)][j % len(matrix[0])]
                for j in range(factor * len(matrix[0]))
            ]
            for i in range(factor * len(matrix))
        ]

    def bfs(self, matrix, start, step_count):
        visited = set()
        queue = deque([(start, 0)])
        while queue:
            (row, col), steps = queue.popleft()
            if steps > step_count:
                continue
            for dr, dc in self.DIRECTIONS:
                new_row, new_col = row + dr, col + dc
                if matrix[new_row][new_col] != self.ROCK and (new_row, new_col) not in visited:
                    visited.add((new_row, new_col))
                    queue.append(((new_row, new_col), steps + 1))
        # since starting point is even, then, you can only reach another point that has coordinates that add
        # up to an even number, if your required steps are even. Reverse logic for odd numbers
        return len(
            [(row, col) for row, col in visited if (row + col) % 2 == step_count % 2]
        )

    @answer((3639, 604592315958630))
    def solve(self) -> tuple[int, int]:
        # assumption that start is in the middle of the matrix
        # this also implies that the dimensions of the matrix is odd
        start = len(self.input) // 2, len(self.input) // 2
        visited = self.bfs(self.input, start, 64)

        expanded = self.expand_matrix(self.input, 7)
        start = len(expanded) // 2, len(expanded) // 2
        y_values = [self.bfs(expanded, start, step_count) for step_count in [65, 196, 327]]
        '''
        65, 65 + 131, 65 + 131 * 2
         
        4444444
        4333334
        4322234
        4321234
        4322234
        4333334
        4444444
        
        (The whole map has 131 rows and columns)
        65 is the number of steps required to reach the edge of the first. 
        To reach the edge between 2 and 3 you need to walk 65 + 131 steps, etc.
        '''
        x_values = np.array([0, 1, 2])

        target = (26501365 - 65) // 131
        coefficients = np.polyfit(x_values, y_values, 2)
        result = np.polyval(coefficients, target)

        return visited, ceil(result)
