# puzzle prompt: https://adventofcode.com/2023/day/22

from ...base import StrSplitSolution, answer
import re
from collections import defaultdict

class Solution(StrSplitSolution):
    _year = 2023
    _day = 22

    # Function is basically a topological sort
    def getDependencies(self, children, n):
        # in-degree is the number of arrows that are pointing to the node and represents the number of children
        # the brick is relying on
        inDeg = defaultdict(int)
        for p, kids in children.items():
            for c in kids:
                inDeg[c] += 1
        depth = -1      # start with -1 because you dont want to count the node that you are removing
        Q = [n]
        while Q:
            current = Q.pop()
            depth += 1
            for c in children[current]:
                inDeg[c] -= 1
                if inDeg[c] == 0:       # this node has no more childing supporting it, so it has to be added to the Q
                    Q.append(c)
        return depth

    @answer((492, 86556))
    def solve(self) -> tuple[int, int]:
        # x1, y1, z1, x2, y2, z2, index
        bricks = [list(map(int, re.findall("-?\d+", l))) + [i] for i, l in enumerate(self.input)]
        bricks.sort(key=lambda b: b[2])     # sort by the z-axis

        sitsOn = defaultdict(set)
        children = defaultdict(set)

        # Stores the Highest Z value, followed by the index of the brick
        highestZ = defaultdict(lambda: (0, -1))
        for brick in bricks:
            x1, y1, z1, x2, y2, z2, ind = brick
            nZ = 0
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    # Trying to get the highest Z value within all combinations of this x & y values
                    nZ = max(nZ, highestZ[complex(x, y)][0])
            height = z2 - z1 + 1
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    old = highestZ[complex(x, y)]
                    # You only care about the highest point (largest Z value) that is touching the new block
                    if old[0] == nZ:
                        # creating a graph of what index brick is sitting on what other brick
                        sitsOn[ind].add(old[1])
                        children[old[1]].add(ind)
                    highestZ[complex(x, y)] = (nZ + height, ind)

        # -1 represents the ground, so we need to delete all the "children" of the ground, that it sits on
        for c in children[-1]:
            del sitsOn[c]
        del children[-1]    # then finally delete the ground itself

        unsafe = set()
        for k, v in sitsOn.items():
            if len(v) == 1:
                # Takes the union of the set, "unsafe" and v
                unsafe |= v
        part1 = len(bricks) - len(unsafe)

        part2 = 0
        for brick in unsafe:
            part2 += self.getDependencies(children, brick)

        return part1, part2
