# puzzle prompt: https://adventofcode.com/2023/day/15
from collections import defaultdict

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2023
    _day = 15

    @answer(511215)
    def part_1(self) -> int:
        res = 0
        for i in self.input[0].split(","):
            res += self.hashAlgo(i)
        return res

    @answer(236057)
    def part_2(self) -> int:
        store = defaultdict(list)
        for i in range(256):
            store[i] = []
        for line in self.input[0].split(","):
            if "-" in line:
                string = line.split("-")
                hashValue = self.hashAlgo(string[0])
                try:
                    for jdx, j in enumerate(store[hashValue]):
                        if j[0] == string[0]:
                            store[hashValue].pop(jdx)
                            break
                except:
                    continue
            else:
                string = line.split("=")
                hashValue = self.hashAlgo(string[0])
                flag = False
                for jdx, j in enumerate(store[hashValue]):
                    if j[0] == string[0]:
                        store[hashValue][jdx] = (string[0], string[1])
                        flag = True
                        break
                if not flag:
                    store[hashValue].append((string[0], string[1]))

        res = 0
        for k, v in store.items():
            for idx, i in enumerate(v):
                res += (k + 1) * (idx + 1) * int(i[1])

        return res

    def hashAlgo(self, string):
        cur = 0
        for i in string:
            cur = ((cur + ord(i)) * 17) % 256
        return cur
