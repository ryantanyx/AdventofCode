# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/3

from ...base import StrSplitSolution, answer
import re
from functools import reduce


class Solution(StrSplitSolution):
    _year = 2023
    _day = 3

    @answer(525911)
    def part_1(self) -> int:
        res = 0
        store = self.getProcessedStore(self.input)
        digitIdx, allDigits = self.getProcessedInputs()

        idxList = []
        for idx, i in enumerate(allDigits):
            pointer = 0
            for j in i:
                idxList.append((j, digitIdx[idx][pointer:pointer + len(j)]))
                pointer += len(j)
        for i in idxList:
            for j in i[1]:
                if store[j[0]][j[1]] == 1:
                    res += int(i[0])
                    break
        return res

    @answer(75805607)
    def part_2(self) -> int:
        res = 0

        digitIdx, allDigits = self.getProcessedInputs()
        idxList = []
        for idx, i in enumerate(allDigits):
            pointer = 0
            for j in i:
                for k in range(len(j)):
                    idxList.append((digitIdx[idx][pointer + k], int(j)))
                pointer += len(j)
        store = self.getProcessedStorePart2(idxList)
        for idx, i in enumerate(self.input):
            for jdx, j in enumerate(i):
                if j == "*":
                    setNum = set(store[idx + i][jdx + j] for i in [-1, 0, 1] for j in [-1, 0, 1])
                    setNum.remove(0)
                    if len(setNum) == 2:
                        res += reduce((lambda x, y: x * y), setNum)
        return res

    """
    Returns a list for index of each digit and a list of all the gear numbers in the original input
    """
    def getProcessedInputs(self):
        digitIdx = []
        for idx, i in enumerate(self.input):
            temp = []
            for jdx, j in enumerate(i):
                if j.isdigit():
                    temp.append((idx, jdx))
            digitIdx.append(temp)
        allDigits = []
        for i in self.input:
            allDigits.append(re.findall(r"(\d+)", i))
        return digitIdx, allDigits

    """
    Returns a 2D array containing 1 if there is a special character beside it, 0 otherwise
    """
    def getProcessedStore(self, data):
        store = [[0 for i in range(len(data[0]))] for j in range(len(data))]
        for idx, i in enumerate(data):
            for jdx, j in enumerate(i):
                if not j.isdigit() and j != ".":
                    if idx == 0 and (jdx != 0 or jdx != len(data[0])):
                        store[idx][jdx + 1] = 1
                        store[idx][jdx - 1] = 1
                        store[idx + 1][jdx] = 1
                        store[idx + 1][jdx + 1] = 1
                        store[idx + 1][jdx - 1] = 1
                    elif idx == len(data) - 1 and (jdx != 0 or jdx != len(data[0])):
                        store[idx][jdx + 1] = 1
                        store[idx][jdx - 1] = 1
                        store[idx - 1][jdx] = 1
                        store[idx - 1][jdx + 1] = 1
                        store[idx - 1][jdx - 1] = 1
                    else:
                        for a in [-1, 0, 1]:
                            for b in [-1, 0, 1]:
                                if a != 0 or b != 0:
                                    store[idx + a][jdx + b] = 1
        return store

    """
    Returns a 2D array containing all the locations where the gear numbers can be found
    eg if 355 spans the first 3 spaces, then array = [[355, 355, 355, ...], ...]
    """
    def getProcessedStorePart2(self, inputs):
        store = [[0 for i in range(len(self.input[0]))] for j in range(len(self.input))]
        for i in inputs:
            store[i[0][0]][i[0][1]] = i[1]
        return store
