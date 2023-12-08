# puzzle prompt: https://adventofcode.com/2023/day/8
import re

from ...base import StrSplitSolution, answer
from math import gcd


class Solution(StrSplitSolution):
    _year = 2023
    _day = 8

    @answer((11567, 9858474970153))
    def solve(self) -> tuple[int, int]:
        directions, store = self.getInputs()

        numDir = len(directions)
        minStepsList = []
        startingNodes = []
        for i in store.keys():
            if i[-1] == "A":
                startingNodes.append(i)

        for i in startingNodes:
            curr = i
            idx = steps = 0
            while True:
                if directions[idx] == "L":
                    curr = store[curr][0]
                else:
                    curr = store[curr][1]

                idx = (idx + 1) % numDir
                steps += 1
                if curr[-1] == "Z":
                    minStepsList.append(steps)
                    break

        lcm = 1
        for i in minStepsList:
            lcm = lcm * i // gcd(lcm, i)

        return minStepsList[0], lcm

    def getInputs(self):
        store = {}
        for i in self.input[2:]:
            s = i.split(" = ")
            store[s[0]] = re.findall("\w+", s[1])

        return self.input[0], store
