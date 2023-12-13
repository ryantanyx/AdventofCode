# puzzle prompt: https://adventofcode.com/2023/day/13
import re

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2023
    _day = 13

    @answer(31956)
    def part_1(self) -> int:
        parsedInput = self.parseInputs()
        # Transpose the input so that the same algorithm can be used to find horizontal slices
        transposedInput = self.transposeInput(parsedInput)
        result = 0
        result += self.getVerticalSliceIdxPart1(parsedInput)
        result += self.getVerticalSliceIdxPart1(transposedInput, 100)

        return result

    @answer(37617)
    def part_2(self) -> int:
        parsedInput = self.parseInputs()
        # Transpose the input so that the same algorithm can be used to find horizontal slices
        transposedInput = self.transposeInput(parsedInput)
        result = 0
        result += self.getVerticalSliceIdxPart2(parsedInput)
        result += self.getVerticalSliceIdxPart2(transposedInput, 100)
        return result

    def getVerticalSliceIdxPart1(self, inputList, multiplier=1):
        res = 0
        for i in inputList:
            for j in range(1, len(i[0])):
                start, end = 0, len(i[0])
                segLen = min(j - start, end - j)
                flag = True
                for k in range(len(i)):
                    mirrorLeft, mirrorRight = i[k][max(0, j - segLen): j], i[k][j: min(end, j + segLen)]
                    leftPattern, rightPattern = re.findall("#+", mirrorLeft), re.findall("#+", mirrorRight)
                    if leftPattern != rightPattern[::-1]:
                        flag = False
                        break
                if flag:
                    res += j * multiplier
                    break
        return res

    def getVerticalSliceIdxPart2(self, inputList, multiplier=1):
        res = 0
        for idx, i in enumerate(inputList):
            for j in range(1, len(i[0])):
                start, end = 0, len(i[0]) - 1
                segLen = min(j - start, end - j + 1)
                flag = True
                mistakes = 0
                for k in range(len(i)):
                    mirrorLeft, mirrorRight = i[k][max(0, j - segLen): j], i[k][j: min(end+1, j + segLen)]
                    lPattern, rPattern = re.findall("#+", mirrorLeft), re.findall("#+", mirrorRight)
                    lPatternLen, rPatternLen = len("".join(z for z in lPattern)), len("".join(z for z in rPattern))
                    if lPattern != rPattern[::-1] or mirrorLeft != mirrorRight[::-1]:
                        # there must be exactly 1 '#' missing and the lengths of the patternArray differ by 1 or 0
                        if (abs(lPatternLen-rPatternLen) == 1 and
                                (len(lPattern) == len(rPattern) or abs(len(lPattern) - len(rPattern)) == 1)):
                            mistakes += 1
                            # Allow for only 1 "mistake". If there are more, means the smudge cant be fixed
                            if mistakes > 1:
                                flag = False
                                break
                        else:
                            flag = False
                if flag and mistakes == 1:
                    res += j * multiplier
                    break
        return res

    def parseInputs(self):
        innerList = []
        parsedInput = []
        for line in self.input:
            if line:
                innerList.append(line)
            else:
                parsedInput.append(innerList)
                innerList = []
        parsedInput.append(innerList)

        return parsedInput

    def transposeInput(self, inputList):
        newParsedInput = []
        for puzzle in inputList:
            innerList = []
            newLineStr = ""
            for idx in range(len(puzzle[0])):
                for k in range(len(puzzle)):
                    newLineStr += puzzle[k][idx]
                innerList.append(newLineStr)
                newLineStr = ""
            newParsedInput.append(innerList)
        return newParsedInput
