# puzzle prompt: https://adventofcode.com/2023/day/17

from ...base import StrSplitSolution, answer
from heapq import heappop, heappush


class Solution(StrSplitSolution):
    _year = 2023
    _day = 17

    def doSearch(self, mini, maxi, grid, x=0):
        end = [*grid][-1]
        todo = [(0, 0, 0, 1), (0, 0, 0, 1j)]
        seen = set()

        while todo:
            val, _, pos, dir = heappop(todo)
            if pos == end:
                return val
            if (pos, dir) in seen:
                continue
            seen.add((pos, dir))

            for d in [1j / dir, -1j / dir]:
                for i in range(mini, maxi + 1):
                    if pos + d * i in grid:
                        v = sum(grid[pos + d * j] for j in range(1, i + 1))
                        heappush(todo, (val + v, (x := x + 1), pos + d * i, d))

    @answer((963, 1178))
    def solve(self) -> tuple[int, int]:
        grid = {i + j * 1j: int(c) for i, r in enumerate(self.input)
                for j, c in enumerate(r.strip())}
        return self.doSearch(1, 3, grid), self.doSearch(4, 10, grid)
