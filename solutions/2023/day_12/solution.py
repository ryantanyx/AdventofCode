# puzzle prompt: https://adventofcode.com/2023/day/12

from ...base import StrSplitSolution, answer
from functools import cache


class Solution(StrSplitSolution):
    _year = 2023
    _day = 12

    @cache
    def count(self, spr: str, num: tuple[int], current: int = 0) -> int:
        if not spr:                     # base case: if spring string is empty
            return not num and not current    # return 1 (True) if num is an empty list and currentCount == 0
        n = 0
        # if current char is '#' or '?', shift to next string char, and increase current by 1
        if spr[0] in ("#", "?"):
            n += self.count(spr[1:], num, current + 1)

        # if current char is '.' or '?' and num Array is not empty and value of current == num[0] or current != 0
        # then shift to next string char, reset current back to 0 (default current = 0 parameter)
        # shift to next value in the num array if current == 1 else, don't shift
        if spr[0] in (".", "?") and (num and num[0] == current or not current):
            n += self.count(spr[1:], num[1:] if current else num)
        return n

    @answer((7286, 25470469710341))
    def solve(self) -> tuple[int, int]:
        springsList = []
        numsList = []
        for i in self.input:
            x1, x2 = i.split(" ")
            springsList.append(x1)
            numsList.append(x2)
        store = [(spr, tuple(int(n) for n in num.split(","))) for spr, num in zip(springsList, numsList)]

        return (sum(self.count(spr + ".", num, 0) for spr, num in store),
                sum(self.count("?".join([p] * 5) + ".", s * 5) for p, s in store))
