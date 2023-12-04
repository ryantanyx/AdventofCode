# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2022/day/4

from ...base import StrSplitSolution, answer
import re


class Solution(StrSplitSolution):
    _year = 2022
    _day = 4

    @answer(477)
    def part_1(self) -> int:
        res = 0
        for i in self.input:
            digits = re.findall(r"(\d+)-(\d+)", i)
            for j in range(0, len(digits), 2):
                if int(digits[j][0]) >= int(digits[j + 1][0]) and int(digits[j][1]) <= int(digits[j + 1][1]):
                    res += 1
                elif int(digits[j + 1][0]) >= int(digits[j][0]) and int(digits[j + 1][1]) <= int(digits[j][1]):
                    res += 1
        return res

    @answer(830)
    def part_2(self) -> int:
        res = 0
        for i in self.input:
            digits = re.findall(r"(\d+)-(\d+)", i)
            for j in range(0, len(digits), 2):
                if int(digits[j][0]) <= int(digits[j + 1][0]) <= int(digits[j][1]):
                    res += 1
                elif int(digits[j][0]) <= int(digits[j + 1][1]) <= int(digits[j][1]):
                    res += 1
                elif int(digits[j + 1][0]) <= int(digits[j][0]) <= int(digits[j + 1][1]):
                    res += 1
                elif int(digits[j + 1][0]) <= int(digits[j][1]) <= int(digits[j + 1][1]):
                    res += 1
        return res
