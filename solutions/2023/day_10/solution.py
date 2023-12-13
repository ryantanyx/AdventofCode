# puzzle prompt: https://adventofcode.com/2023/day/10
import copy

from ...base import StrSplitSolution, answer
from collections import deque


class Solution(StrSplitSolution):
    _year = 2023
    _day = 10
    # NB Check your input, if 'S' behaves like "|", "J", "L", then leave
    # 'S' in array, otherwise remove it
    array = ["|", "J", "L", "S"]

    @answer(7102)
    def part_1(self) -> int:
        paddedInput = self.getPaddedInput()
        start = self.getInputs(paddedInput)
        store = [[-1 for i in range(len(paddedInput[0]))] for j in range(len(paddedInput))]
        store[start[0]][start[1]] = 0
        v = set()
        q = deque([start])
        while q:
            x, y = q.popleft()  # returns the coordinates
            if (x, y) not in v:
                v.add((x, y))
                if paddedInput[x - 1][y] in ['|', '7', 'F']:
                    if (x - 1, y) not in v:
                        q.append((x - 1, y))
                        store[x - 1][y] = store[x][y] + 1

                if paddedInput[x + 1][y] in ['|', 'L', 'J']:
                    if (x + 1, y) not in v:
                        q.append((x + 1, y))
                        store[x + 1][y] = store[x][y] + 1

                if paddedInput[x][y - 1] in ['-', 'L', 'F']:
                    if (x, y - 1) not in v:
                        q.append((x, y - 1))
                        store[x][y - 1] = store[x][y] + 1

                if paddedInput[x][y + 1] in ['J', '-', '7']:
                    if (x, y + 1) not in v:
                        q.append((x, y + 1))
                        store[x][y + 1] = store[x][y] + 1

        maxi = -1
        for j in store:
            maxi = max(maxi, max(j))
        return maxi

    @answer(363)
    def part_2(self) -> int:
        pass


    def getInputs(self, paddedInput):
        for i in range(len(paddedInput)):
            for j in range(len(paddedInput[0])):
                if paddedInput[i][j] == 'S':
                    return i, j

    def getPaddedInput(self):
        tmp = copy.deepcopy(self.input)
        tmp.insert(0, "." * len(self.input))
        tmp.append("." * len(self.input))
        res = []
        for j in tmp:
            res.append("." + j + ".")
        return res

    def getPaddedInput2(self):
        tmp = copy.deepcopy(self.input)
        tmp.insert(0, "." * len(self.input))
        tmp.append("." * len(self.input))
        res = []
        for j in tmp:
            t1 = ["."]
            t1.extend([j[i] for i in range(len(j))])
            t1.append(".")
            res.append(t1)
        return res

    def getNumberOfTilesLeft(self, grid, i, j):
        cnt = 0
        for idx in range(j):
            if grid[i][idx] in self.array:
                cnt += 1
        return cnt

    @answer((7102, 363))
    def solve(self) -> tuple[int, int]:
        grid = self.getPaddedInput2()
        lenGrid = [[-1 for i in range(len(grid[0]))] for j in range(len(grid))]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'S':
                    lenGrid[i][j] = 0
                    if grid[i - 1][j] in ['|', '7', 'F']:
                        lenGrid[i - 1][j] = 1
                    if grid[i + 1][j] in ['|', 'L', 'J']:
                        lenGrid[i + 1][j] = 1
                    if grid[i][j + 1] in ['J', '-', '7']:
                        lenGrid[i][j + 1] = 1
                    if grid[i][j - 1] in ['-', 'L', 'F']:
                        lenGrid[i][j - 1] = 1

        def changeLenGrid(i, j, wasChange):
            if lenGrid[i][j] == -1:
                lenGrid[i][j] = steps + 1
                return True
            return wasChange

        steps = 0
        wasChange = True
        while wasChange:
            wasChange = False
            steps += 1
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if lenGrid[i][j] == steps:
                        # can you move up
                        if grid[i][j] in ['|', 'L', 'J'] and grid[i - 1][j] in ['|', '7', 'F']:
                            wasChange = changeLenGrid(i - 1, j, wasChange)

                        # can you move down:
                        if grid[i][j] in ['|', '7', 'F'] and grid[i + 1][j] in ['|', 'L', 'J']:
                            wasChange = changeLenGrid(i + 1, j, wasChange)

                        # can you move right
                        if grid[i][j] in ['-', 'L', 'F'] and grid[i][j + 1] in ['J', '-', '7']:
                            wasChange = changeLenGrid(i, j + 1, wasChange)

                        # can you move left
                        if grid[i][j] in ['J', '-', '7'] and grid[i][j - 1] in ['-', 'L', 'F']:
                            wasChange = changeLenGrid(i, j - 1, wasChange)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if lenGrid[i][j] == -1:
                    grid[i][j] = "."

        part2Sum = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == ".":
                    numOfTilesLeft = self.getNumberOfTilesLeft(grid, i, j)
                    if numOfTilesLeft % 2 == 1:
                        part2Sum += 1

        return steps, part2Sum
