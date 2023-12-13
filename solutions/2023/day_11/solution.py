# puzzle prompt: https://adventofcode.com/2023/day/11
import re

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2023
    _day = 11

    def getGalaxyCoords(self, grid):
        coords = []
        for idx, i in enumerate(grid):
            s = "".join(i)
            matches = re.finditer("#", s)
            for match in matches:
                coords.append((idx, match.start()))
        return coords

    def getEmptyRC(self):
        toExpand = []
        toExpand2 = []
        grid = [[i for i in j] for j in self.input]
        for i in range(len(self.input)):
            flag = True
            for j in range(len(self.input[0])):
                if self.input[i][j] == "#":
                    flag = False
                    break
            if flag:
                toExpand.append(i)
        for i in range(len(self.input[0])):
            flag = True
            for j in range(len(self.input)):
                if self.input[j][i] == "#":
                    flag = False
                    break
            if flag:
                toExpand2.append(i)
        return toExpand, toExpand2, grid

    @answer((10494813, 840988812853))
    def solve(self) -> tuple[int, int]:
        expansionP1 = 2
        expansionP2 = 1000000
        R, C, grid = self.getEmptyRC()
        coords = self.getGalaxyCoords(grid)
        part1Sum = part2Sum = 0
        for idx, i in enumerate(coords):
            for j in range(idx + 1, len(coords)):
                min_x, max_x = min(i[0], coords[j][0]), max(i[0], coords[j][0])
                min_y, max_y = min(i[1], coords[j][1]), max(i[1], coords[j][1])
                for k in range(min_x + 1, max_x + 1):
                    part1Sum += expansionP1 if k in R else 1
                    part2Sum += expansionP2 if k in R else 1
                for l in range(min_y + 1, max_y + 1):
                    part1Sum += expansionP1 if l in C else 1
                    part2Sum += expansionP2 if l in C else 1
        return part1Sum, part2Sum
