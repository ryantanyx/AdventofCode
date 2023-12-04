# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2022/day/1

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2022
    _day = 1

    @answer((67027, 197291))
    def solve(self) -> tuple[int, int]:
        res = []
        totalCal = 0
        for i in self.input:
            if i.isdigit():
                totalCal += int(i)
            else:
                res.append(totalCal)
                totalCal = 0
        res.sort(reverse=True)
        return res[0], sum(res[:3])
