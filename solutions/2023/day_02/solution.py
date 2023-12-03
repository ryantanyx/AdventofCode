# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template
from collections import defaultdict

# puzzle prompt: https://adventofcode.com/2023/day/2

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2023
    _day = 2

    def getState(self, singleInput):
        singleInput = singleInput.split(": ")[1].split("; ")
        state = {"red": 0, "blue": 0, "green": 0}
        for i in singleInput:
            take = i.split(", ")
            for j in take:
                splitStr = j.split(" ")
                state[splitStr[1]] = max(state[splitStr[1]], int(splitStr[0]))
        return state

    @answer((2720, 71535))
    def solve(self) -> tuple[int, int]:
        modifiedState = []
        part1Res = 0
        part2Res = 0
        for idx, i in enumerate(self.input):
            modifiedState.append((idx + 1, self.getState(i)))
        for i, j in modifiedState:
            if j["red"] <= 12 and j["green"] <= 13 and j["blue"] <= 14:
                part1Res += i
            part2Res += j["red"] * j["green"] * j["blue"]
        return part1Res, part2Res
