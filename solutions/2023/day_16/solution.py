# puzzle prompt: https://adventofcode.com/2023/day/16

from ...base import StrSplitSolution, answer
from collections import deque


class Solution(StrSplitSolution):
    _year = 2023
    _day = 16

    @answer(7939)
    def part_1(self) -> int:
        grid = [[j for j in i] for i in self.input]
        height, width = len(self.input) - 1, len(self.input[0]) - 1
        return self.runFullSearch(grid, height, width)

    @answer(8318)
    def part_2(self) -> int:
        grid = [[j for j in i] for i in self.input]
        height, width = len(self.input) - 1, len(self.input[0]) - 1
        possibleStarting = []
        for i in range(0, len(self.input[0])):
            possibleStarting.append(((0, i), "D"))
            possibleStarting.append(((height, i), "U"))
        for i in range(0, len(self.input)):
            possibleStarting.append(((i, 0), "R"))
            possibleStarting.append(((i, width), "L"))
        final = []
        for start in possibleStarting:
            final.append(self.runFullSearch(grid, height, width, start))
        return max(final)

    def runFullSearch(self, grid, height, width, start=((0, 0), "R")):
        q = deque([])
        q.append(start)
        v = set()
        while q:
            cur, dir = q.popleft()
            if (cur, dir) in v:
                continue
            v.add((cur, dir))
            if grid[cur[0]][cur[1]] == ".":
                if dir == "R":
                    q = self.turnRight(cur, q, width)
                elif dir == "L":
                    q = self.turnLeft(cur, q, width)
                elif dir == "D":
                    q = self.turnDown(cur, q, height)
                elif dir == "U":
                    q = self.turnUp(cur, q, height)
            elif grid[cur[0]][cur[1]] == "|":
                if dir == "R" or dir == "L":
                    q = self.turnDown(cur, q, height)
                    q = self.turnUp(cur, q, height)
                elif dir == "D":
                    q = self.turnDown(cur, q, height)
                elif dir == "U":
                    q = self.turnUp(cur, q, height)
            elif grid[cur[0]][cur[1]] == "-":
                if dir == "D" or dir == "U":
                    q = self.turnRight(cur, q, width)
                    q = self.turnLeft(cur, q, width)
                elif dir == "R":
                    q = self.turnRight(cur, q, width)
                elif dir == "L":
                    q = self.turnLeft(cur, q, width)
            elif grid[cur[0]][cur[1]] == "\\":
                if dir == "D":
                    q = self.turnRight(cur, q, width)
                elif dir == "R":
                    q = self.turnDown(cur, q, height)
                elif dir == "L":
                    q = self.turnUp(cur, q, height)
                elif dir == "U":
                    q = self.turnLeft(cur, q, width)
            elif grid[cur[0]][cur[1]] == "/":
                if dir == "D":
                    q = self.turnLeft(cur, q, width)
                elif dir == "L":
                    q = self.turnDown(cur, q, height)
                elif dir == "R":
                    q = self.turnUp(cur, q, height)
                elif dir == "U":
                    q = self.turnRight(cur, q, width)
        res = set()
        for i, _ in v:
            res.add(i)
        return len(res)

    def turnLeft(self, cur, q, width):
        if 0 <= (cur[1] - 1) <= width:
            q.append(((cur[0], cur[1] - 1), "L"))
        return q

    def turnRight(self, cur, q, width):
        if 0 <= (cur[1] + 1) <= width:
            q.append(((cur[0], cur[1] + 1), "R"))
        return q

    def turnUp(self, cur, q, height):
        if 0 <= (cur[0] - 1) <= height:
            q.append(((cur[0] - 1, cur[1]), "U"))
        return q

    def turnDown(self, cur, q, height):
        if 0 <= (cur[0] + 1) <= height:
            q.append(((cur[0] + 1, cur[1]), "D"))
        return q
