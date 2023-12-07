# puzzle prompt: https://adventofcode.com/2023/day/5


import re
from collections import deque
from copy import deepcopy

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2023
    _day = 5

    @answer(486613012)
    def part_1(self) -> int:
        smallest = 999999999999999999
        seeds, allMappings = self.getInputs()
        for seed in seeds:
            mapped = seed
            for j in allMappings:
                for k in j:
                    if k[1] <= mapped <= (k[1] + k[2] - 1):
                        mapped = k[0] + (mapped - k[1])
                        break
            smallest = min(smallest, mapped)
        return smallest

    @answer(56931769)
    def part_2(self) -> int:
        globalMin = 999999999999999999
        a, b = self.getInputs()
        for i in range(0, len(a), 2):
            # range is stored as (s, e), where s is inclusive and e is exclusive
            oldRange = deque([(a[i], a[i] + a[i + 1])])
            for seedMapping in b:
                new = []
                while oldRange:
                    current = oldRange.popleft()
                    s, e = current[0], current[1]
                    flag = False
                    for oneMapping in seedMapping:
                        start, end = oneMapping[1], oneMapping[1] + oneMapping[2]
                        if s <= start:
                            if start < e <= end:
                                # Case for:
                                # ---- s ---- start ---- e ------ end ----
                                new.append((oneMapping[0], oneMapping[0] + (e - start)))
                                oldRange.append((s, start))
                                flag = True
                                break
                            elif e > end:
                                # Case for:
                                # ---- s ---- start ---- end ------ e ----
                                new.append((oneMapping[0], oneMapping[0] + oneMapping[2]))
                                oldRange.append((end, e))
                                oldRange.append((s, start))
                                flag = True
                                break
                        else:
                            if s < end:
                                if start < e <= end:
                                    # Case for:
                                    # ---- start ---- s ---- e ------ end ----
                                    new.append((oneMapping[0] + (s - start), oneMapping[0] + (e - start)))
                                    flag = True
                                    break
                                else:
                                    # Case for:
                                    # ---- start ---- s ---- end ------ e ----
                                    new.append((oneMapping[0] + (s - start), oneMapping[0] + oneMapping[2]))
                                    flag = True
                                    oldRange.append((end, e))
                                    break
                    if not flag:
                        # if s and e are unchanged, then propagate the range to the next mapping
                        new.append((s, e))
                oldRange = deque(deepcopy(new))
                new = []

            while (0, 0) in oldRange:
                oldRange.remove((0, 0))
            curMin = min([i[0] for i in oldRange])
            globalMin = min(curMin, globalMin)

        return globalMin

    def getInputs(self):
        seeds = [int(i) for i in re.findall(r"\d+", self.input[0])]
        res = []
        newArray = []
        for i in self.input[1:]:

            if i == "":
                res.append(newArray)
                newArray = []
                continue
            if i[0].isdigit():
                newArray.append([int(j) for j in re.findall(r"\d+", i)])
        res.append(newArray)
        return seeds, res[1:]
