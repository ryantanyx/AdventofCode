# puzzle prompt: https://adventofcode.com/2023/day/6
import re

from ...base import StrSplitSolution, answer
from functools import reduce

class Solution(StrSplitSolution):
    _year = 2023
    _day = 6

    @answer(227850)
    def part_1(self) -> int:
        time, dist = self.getInputs()
        res = []

        for jdx, j in enumerate(dist):
            tmp = 0
            for i in range(1, time[jdx]):
                if (time[jdx] - i) * i > dist[jdx]:
                    tmp += 1
            res.append(tmp)
        return reduce(lambda x, y: x * y, res)

    @answer(42948149)
    def part_2(self) -> int:
        time, dist = self.getInputs()
        time = int("".join(str(i) for i in time))
        dist = int("".join(str(i) for i in dist))
        res = 0
        for i in range(1, time):
            if (time - i) * i > dist:
                res += 1
        return res

    def getInputs(self):
        time = [int(i) for i in re.findall("\d+", self.input[0])]
        dist = [int(i) for i in re.findall("\d+", self.input[1])]
        return time, dist
