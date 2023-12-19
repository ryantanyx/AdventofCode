# puzzle prompt: https://adventofcode.com/2023/day/19

from collections import defaultdict
from copy import deepcopy
from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2023
    _day = 19

    @answer(432427)
    def part_1(self) -> int:
        store, partsList = self.parseInputs()
        res = 0
        for part in partsList:
            cur = "in"
            path = [cur]        # path is not needed in this qn
            while True:
                criteria = store[cur]
                flag = False
                for oneCriteria in criteria[:-1]:
                    if oneCriteria[0] in part.keys():
                        if oneCriteria[1] == "<" and part[oneCriteria[0]] < oneCriteria[2]:
                            cur = oneCriteria[3]
                            flag = True
                            path.append(cur)
                            break
                        elif oneCriteria[1] == "<" and part[oneCriteria[0]] >= oneCriteria[2]:
                            continue
                        elif oneCriteria[1] == ">" and part[oneCriteria[0]] > oneCriteria[2]:
                            cur = oneCriteria[3]
                            flag = True
                            path.append(cur)
                            break
                        elif oneCriteria[1] == ">" and part[oneCriteria[0]] <= oneCriteria[2]:
                            continue
                if not flag:
                    if cur == "A":
                        res += sum(part.values())
                        break
                    elif cur == "R":
                        break
                    else:
                        cur = criteria[-1]
                        path.append(cur)
                if flag:
                    continue
        return res

    @answer(143760172569135)
    def part_2(self) -> int:
        store, partsList = self.parseInputs()
        allPaths = []
        cur = "in"
        q = [([cur], [])]
        while q:
            cur, conditionList = q.pop()
            if cur[-1] == "A":
                if conditionList not in allPaths and conditionList != []:
                    allPaths.append(conditionList)
                continue
            if cur[-1] == "R":
                continue
            criteria = store[cur[-1]]
            tmp = []
            secondary = deepcopy(cur)
            conditionList2 = deepcopy(conditionList)
            for oneCriteria in criteria[:-1]:
                t1 = deepcopy(conditionList)
                t1.append(oneCriteria[:-1])
                t2 = deepcopy(cur)
                t2.append(oneCriteria[-1])
                q.append((t2, t1))
                if oneCriteria[1] == "<":
                    tmp.append((oneCriteria[0], ">", oneCriteria[2] - 1))
                elif oneCriteria[1] == ">":
                    tmp.append((oneCriteria[0], "<", oneCriteria[2] + 1))
                conditionList.extend(tmp)
                cur = t2

            secondary.append(criteria[-1])
            conditionList2.extend(tmp)
            q.append((secondary, conditionList2))
        res = 0
        for path in allPaths:
            finalDict = {'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000]}
            for cond in path:
                if cond[1] == ">":
                    finalDict[cond[0]][0] = max(cond[2] + 1, finalDict[cond[0]][0])
                if cond[1] == "<":
                    finalDict[cond[0]][1] = min(cond[2] - 1, finalDict[cond[0]][1])
            ranges = [abs(i[0] - i[1]) + 1 for i in finalDict.values()]
            res += ranges[0] * ranges[1] * ranges[2] * ranges[3]
        return res

    def parseInputs(self):
        store = defaultdict(list)
        for idx, i in enumerate(self.input):
            if i != "":
                a, b = i.split("{")
                b.strip("}")
                test = b.split(",")
                for j in test[:-1]:
                    d, e = j.split(":")
                    store[a].append((d[0], d[1], int(d[2:]), e))
                store[a].append(test[-1].strip("}"))
            else:
                break
        partsList = []
        for i in range(idx + 1, len(self.input)):
            a = self.input[i].strip("{}").split(",")
            test = {}
            for j in a:
                b = j.split("=")
                test[b[0]] = int(b[1])
            partsList.append(test)
        return store, partsList
