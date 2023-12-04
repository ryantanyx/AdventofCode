# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2022/day/2

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2022
    _day = 2

    @answer(13446)
    def part_1(self) -> int:
        # Rock (A,X), Paper (B,Y), Scissors (C,Z)
        score = {'A X': 3, "A Y": 6, "A Z": 0, "B X": 0, "B Y": 3, "B Z": 6, "C X": 6, "C Y": 0, "C Z": 3}
        choice = {'X': 1, "Y": 2, "Z": 3}
        return sum([score[j] + choice[j[-1]] for j in self.input])

    @answer(13509)
    def part_2(self) -> int:
        # Rock (A,X), Paper (B,Y), Scissors (C,Z)
        score = {'A X': 3, "A Y": 1, "A Z": 2, "B X": 1, "B Y": 2, "B Z": 3, "C X": 2, "C Y": 3, "C Z": 1}
        choice = {'X': 0, "Y": 3, "Z": 6}
        return sum([score[j] + choice[j[-1]] for j in self.input])

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
