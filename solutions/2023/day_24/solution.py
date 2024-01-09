# puzzle prompt: https://adventofcode.com/2023/day/24

from ...base import StrSplitSolution, answer
import numpy as np
import re


class Solution(StrSplitSolution):
    _year = 2023
    _day = 24

    left = 200000000000000
    right = 400000000000000
    total = 0

    @answer(18651)
    def part_1(self) -> int:
        pts = [[int(y) for y in re.findall(r'-?[0-9]+', x)] for x in self.input]

        total = 0
        for i in range(len(pts) - 1):
            for j in range(i + 1, len(pts)):
                if self.check(pts[i], pts[j]):
                    total += 1

        return total

    @answer(546494494317645)
    def part_2(self) -> int:
        pts = [[int(y) for y in re.findall(r'-?[0-9]+', x)] for x in self.input]

        # define a shift for the first 8 vectors to help with numpy roundoff errors
        shift = min([x for y in pts[:8] for x in y[:3]])

        # shift the first 8 vectors
        for i in range(8):
            for j in range(3):
                pts[i][j] -= shift

        rows1, rows2 = [], []
        col1, col2 = [], []
        ans = []

        for i in range(0, 8, 2):
            # get rows of A in solving for
            row, num = self.calcs(*(pts[i][:2] + pts[i][3:5]), *((pts[i + 1][:2] + pts[i + 1][3:5])))
            rows1.append(row)
            col1.append(num)
            # populate solving for a, c, d, f
            row, num = self.calcs(*([pts[i][0], pts[i][2], pts[i][3], pts[i][5]]),
                                  *([pts[i + 1][0], pts[i + 1][2], pts[i + 1][3], pts[i + 1][5]]))
            rows2.append(row)
            col2.append(num)

        A = np.array(rows1)
        col = np.array(col1)
        # (a, b, e, f)
        ans1 = np.linalg.solve(A, col)

        A = np.array(rows2)
        col = np.array(col2)
        # (a, c, d, f) :
        ans2 = np.linalg.solve(A, col)

        # add up a, b, c, and shift back (3 * shift) to help with the roundoff errors
        return round(ans1[0]) + round(ans1[1]) + round(ans2[1]) + 3 * shift

    def calcs(self, x1, y1, dx1, dy1, x2, y2, dx2, dy2):
        return [dy2 - dy1, dx1 - dx2, y2 - y1, x2 - x1], y1 * dx1 - y2 * dx2 + x2 * dy2 - x1 * dy1

    def check(self, one, two):
        # b values or positions, v values are velocities
        b1x, b1y, b1z = one[:3]
        b2x, b2y, b2z = two[:3]
        v1x, v1y, v2y = one[3:]
        v2x, v2y, v2z = two[3:]
        # used to prevent unnecessary calculations
        good = True
        if v1x * v2y - v2x * v1y == 0:
            good = False

        if good:
            # find x and y intersecting
            # turn parametric equations x(t) = vx * t + bx, y(t) = vy* t + by into  y = mx + b by solving for m and b
            # then use these equations to calculate the intersection between two such equations,  noting that:
            # m = vy / vx, b = by - vy/vx * bx
            x = -(v1x * v2x * (b1y - b2y) + v1x * v2y * b2x - v2x * v1y * b1x) / (v2x * v1y - v1x * v2y)
            y = -(v1y * v2y * (b1x - b2x) + v1y * v2x * b2y - v2y * v1x * b1y) / (v2y * v1x - v1y * v2x)
            if not (self.left <= x <= self.right) or not (self.left <= y <= self.right):
                # if the intersection is not in range
                good = False
            if good:
                # x = vx * t + b ->  t = (x - b)
                if ((v1x != 0 and (x - b1x) / v1x < 0) or (v2x != 0 and (x - b2x) / v2x < 0)) or (
                        (v1y != 0 and ((y - b1y) / v1y < 0)) or (v2y != 0 and (y - b2y) / v2y < 0)):
                    good = False
        if good:
            return True
        else:
            return False
