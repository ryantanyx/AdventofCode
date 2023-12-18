# puzzle prompt: https://adventofcode.com/2023/day/18

from ...base import StrSplitSolution, answer
import numpy as np


class Solution(StrSplitSolution):
    _year = 2023
    _day = 18

    @answer(42317)
    def part_1(self) -> int:
        store = [[i for i in j.split(" ")] for j in self.input]
        start = end = 0
        res = [(start, end)]
        for dir, num, _ in store:
            num = int(num)
            if dir == "R":
                end += num
            elif dir == "L":
                end -= num
            elif dir == "D":
                start += num
            elif dir == "U":
                start -= num
            res.append((start, end))
        area = self.shoelace(res)
        amtOfLava, pointsOnEdge = self.numOfInteriorPoints(area, res)
        return int(amtOfLava) + pointsOnEdge

    @answer(83605563360288)
    def part_2(self) -> int:
        store = [[i for i in j.split(" ")] for j in self.input]
        newStore = []
        for _, _, colour in store:
            text = colour.strip("(#)")
            if text[-1] == "0":
                dir = "R"
            elif text[-1] == "1":
                dir = "D"
            elif text[-1] == "2":
                dir = "L"
            elif text[-1] == "3":
                dir = "U"
            newStore.append((dir, int(text[:5], 16)))

        start = end = 0
        res = [(start, end)]
        for dir, num in newStore:
            if dir == "R":
                end += num
            elif dir == "L":
                end -= num
            elif dir == "D":
                start += num
            elif dir == "U":
                start -= num
            res.append((start, end))
        area = self.shoelace(res)
        amtOfLava, pointsOnEdge = self.numOfInteriorPoints(area, res)
        return int(amtOfLava) + pointsOnEdge

    def shoelace(self, x_y):
        x_y = np.array(x_y, dtype='int64')
        x_y = x_y.reshape(-1, 2)

        x = x_y[:, 0]
        y = x_y[:, 1]

        S1 = np.sum(x * np.roll(y, -1))
        S2 = np.sum(y * np.roll(x, -1))

        area = .5 * np.absolute(S1 - S2)

        return area

    def numOfInteriorPoints(self, area, res):
        B = 0
        for i in range(1, len(res)):
            if res[i][1] != res[i - 1][1]:
                B += abs(res[i][1] - res[i - 1][1])
            if res[i][0] != res[i - 1][0]:
                B += abs(res[i][0] - res[i - 1][0])
        B += 1
        return (2 * area - B + 2) // 2, B
