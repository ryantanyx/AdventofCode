# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template
import re

# puzzle prompt: https://adventofcode.com/2022/day/5

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2022
    _day = 5

    @answer("JDTMRWCQJ")
    def part_1(self) -> str:
        initialStack, inputs = self.getStartingStackAndInputs()
        for i in inputs:
            for j in range(int(i[0])):
                tmp = initialStack[int(i[1])].pop()
                initialStack[int(i[2])].append(tmp)
        return "".join(i.pop() for i in initialStack[1:])


    @answer("VHJDDCWRD")
    def part_2(self) -> str:
        initialStack,inputs = self.getStartingStackAndInputs()
        for i in inputs:
            tmp = initialStack[int(i[1])][-int(i[0]):]
            initialStack[int(i[2])].extend(tmp)
            initialStack[int(i[1])] = initialStack[int(i[1])][:-int(i[0])]
        return "".join(i.pop() for i in initialStack[1:])

    def getStartingStackAndInputs(self):
        inputs = []
        for i in self.input:
            inputs.append(re.findall("(\d+)", i))
        return [[], ['F', 'H', 'B', 'V', 'R', 'Q', 'D', 'P'], ['L', 'D', 'Z', 'Q', 'W', 'V'],
                ['H', 'L', 'Z', 'Q', 'G', 'R', 'P', 'C'], ['R', 'D', 'H', 'F', 'J', 'V', 'B'],
                ['Z', 'W', 'L', 'C'], ['J', 'R', 'P', 'N', 'T', 'G', 'V', 'M'],
                ['J', 'R', 'L', 'V', 'M', 'B', 'S'], ['D', 'P', 'J'], ['D', 'C', 'N', 'W', 'V']], inputs
