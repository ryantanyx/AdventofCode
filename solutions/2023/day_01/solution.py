# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/1

from ...base import TextSolution, StrSplitSolution, answer
import re

class Solution(StrSplitSolution):
    _year = 2023
    _day = 1

    @answer(53651)
    def part_1(self) -> int:
        res = self.getDigits(self.input)
        return sum(res)

    def getDigits(self, input):
        res = []
        for i in input:
            digit = re.sub('\D', '', i)
            res.append(int(digit[0] + digit[-1]))
        return res

    @answer(53894)
    def part_2(self) -> int:
        store = {"one" : "1", "two" :"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
        newList = []
        for i in self.input:
            for k, v in store.items():
                if k in i:
                    i = i.replace(k, k[0] + v + k[-1])
            newList.append(i)

        digitList = self.getDigits(newList)
        return sum(digitList)