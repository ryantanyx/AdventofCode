# puzzle prompt: https://adventofcode.com/2023/day/4

from ...base import StrSplitSolution, answer
import re
from collections import defaultdict


class Solution(StrSplitSolution):
    _year = 2023
    _day = 4

    @answer(15268)
    def part_1(self) -> int:
        preprocessed = []
        res = 0
        for i in self.input:
            preprocessed.append(self.getNumList(i))
        for j in preprocessed:
            numMatches = 0
            for k in j[0][1:]:
                if k in j[1]:
                    numMatches += 1  # Count number of matches
            if numMatches >= 1:
                res += 2 ** (numMatches - 1)  # Only add to res if there is at least 1 match
        return res


    @answer(6283755)
    def part_2(self) -> int:
        preprocessed = []
        numMatchesList = []
        NumInstancesDict = defaultdict(int)
        for i in self.input:
            preprocessed.append(self.getNumList(i))
        for j in preprocessed:
            numMatch = 0
            for k in j[0][1:]:
                if k in j[1]:
                    numMatch += 1
            numMatchesList.append(numMatch)     # Calculate a list of all the number of matches for each card
        for i in range(1, len(preprocessed) + 1):
            NumInstancesDict[i] = 1         # Initializing a dict with all card instances = 1 (original copy)
        for idx, i in enumerate(numMatchesList):
            for j in range(idx + 2, idx + 2 + i):
                # For each card, add the number of extra copies of cards won to the future card instances (builds the dict)
                NumInstancesDict[j] += NumInstancesDict[idx + 1]
        return sum([i for i in NumInstancesDict.values()])

    """
    Returns a list containing 2 list;
    1st containing all the winning numbers, 2nd containing all the numbers you have
    """
    def getNumList(self, data) -> list:
        a, b = data.split("|")
        return [[int(i) for i in re.findall("(\d+)", a)], [int(i) for i in re.findall("(\d+)", b)]]
