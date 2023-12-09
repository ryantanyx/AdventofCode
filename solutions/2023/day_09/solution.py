# puzzle prompt: https://adventofcode.com/2023/day/9
import re

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2023
    _day = 9

    def getInputs(self):
        inputs = []
        for i in self.input:
            inputs.append([int(j) for j in re.findall("-?\d+", i)])
        return inputs

    def getDiffList(self, original):
        res = []
        for idx in range(len(original)-1):
            res.append(original[idx+1] - original[idx])
        return res

    @answer((2043183816, 1118))
    def solve(self) -> tuple[int, int]:
        puzzles = self.getInputs()
        part1Total = part2Total = 0
        for i in puzzles:
            idx = 0
            store = [i]
            while True:
                new = self.getDiffList(store[idx])
                store.append(new)
                if len(set(new)) == 1:
                    part1 = part2 = store[-1][-1]
                    for j in store[-2::-1]:
                        part2 = j[0] - part2
                        part1 += j[-1]
                    part1Total += part1
                    part2Total += part2
                    break
                idx += 1
        return part1Total, part2Total
