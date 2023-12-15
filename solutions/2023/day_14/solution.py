# puzzle prompt: https://adventofcode.com/2023/day/14
import re

from ...base import StrSplitSolution, answer
from copy import deepcopy


class Solution(StrSplitSolution):
    _year = 2023
    _day = 14
    N = []

    @answer(103614)
    def part_1(self) -> int:
        newInput = self.rotateAnticlockwise90(self.input)
        newInput = self.tiltGridLeft(newInput)
        l = len(newInput)
        store = []
        for i in newInput:
            store.append([(match[0], match.start(), match.end()) for match in re.finditer("O+|#+", i)])
        res = 0
        for idx, i in enumerate(store):
            cur = l
            for j in i:
                if "#" not in j[0]:
                    for k in range(cur, cur - (j[2] - j[1]), -1):
                        res += k
                    cur -= (j[2] - j[1])
                else:
                    cur = l - j[2]

        return res

    @answer(83790)
    def part_2(self) -> int:
        memory = []
        currentList = deepcopy(self.input)

        for i in range(10000):
            if currentList in memory:
                startingIdx = memory.index(currentList)
                break
            else:
                memory.append(currentList)

            currentList = self.doOneCycle(i%4, currentList)

        endIdx = ((4*1000000000) - (startingIdx + 1)) % (i - startingIdx) + startingIdx + 1
        newInput = self.rotateAnticlockwise90(memory[endIdx])
        store = []
        for i in newInput:
            store.append([(match[0], match.start(), match.end()) for match in re.finditer("O", i)])
        res = 0
        l = len(newInput[0])
        for idx, i in enumerate(store):
            cur = l
            for j in i:
                res += (cur - j[1])
        return res

    def tiltGridLeft(self, listI):
        store = []
        gridLen = len(listI)

        for i in listI:
            store.append([(match[0], match.start(), match.end()) for match in re.finditer("O+|#+", i)])

        newGrid = []
        for idx, i in enumerate(listI):
            cur = 0
            newS = ""
            for j in store[idx]:
                if "#" not in j[0]:
                    newS += j[0]
                    cur += (j[2] - j[1])
                else:
                    newS += "." * (j[1] - cur)
                    newS += j[0]
                    cur = j[2]
            newS += "." * (gridLen - cur)
            newGrid.append(newS)
        return newGrid

    def transpose(self, gridI):
        newTmp = []
        for j in range(len(gridI[0])):
            newS = ""
            for i in range(len(gridI)):
                newS += gridI[i][j]
            newTmp.append(newS)
        return newTmp

    def rotateClockwise90(self, gridI):
        newTmp = []
        for j in range(len(gridI[0])):
            newS = ""
            for i in range(len(gridI)-1, -1, -1):
                newS += gridI[i][j]
            newTmp.append(newS)
        return newTmp

    def rotateAnticlockwise90(self, gridI):
        newTmp = []
        for i in range(len(gridI[0])-1, -1, -1):
            newS = ""
            for j in range(len(gridI)-1, -1, -1):
                newS = gridI[j][i] + newS
            newTmp.append(newS)
        return newTmp

    def doOneCycle(self, i, currentList):
        if i == 0:
            currentList = self.rotateAnticlockwise90(currentList)
            currentList = self.tiltGridLeft(currentList)
            currentList = self.rotateClockwise90(currentList)
        elif i == 1:
            currentList = self.tiltGridLeft(currentList)
        elif i == 2:
            currentList = self.rotateClockwise90(currentList)
            currentList = self.tiltGridLeft(currentList)
            currentList = self.rotateAnticlockwise90(currentList)
        elif i == 3:
            currentList = [i[::-1] for i in currentList]
            currentList = self.tiltGridLeft(currentList)
            currentList = [i[::-1] for i in currentList]
        return currentList
