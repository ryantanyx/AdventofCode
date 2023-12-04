# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2022/day/3

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2022
    _day = 3

    @answer(8072)
    def part_1(self) -> int:
        res = 0
        for i in self.input:
            s1, s2 = set(i[:len(i)//2]), set(i[len(i)//2:])
            s3 = s1.intersection(s2)
            letter = s3.pop()
            if letter.islower():
                res += ord(letter) - ord('a') + 1
            else:
                res += ord(letter) - ord('A') + 1 + 26
        return res

    @answer(2567)
    def part_2(self) -> int:
        res = 0
        for i in range(0, len(self.input), 3):
            s1, s2, s3 = set(self.input[i]), set(self.input[i+1]), set(self.input[i+2])
            s4 = s1.intersection(s2).intersection(s3)
            letter = s4.pop()
            if letter.islower():
                res += ord(letter) - ord('a') + 1
            else:
                res += ord(letter) - ord('A') + 1 + 26
        return res
