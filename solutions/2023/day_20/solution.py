# puzzle prompt: https://adventofcode.com/2023/day/20

from ...base import StrSplitSolution, answer
from collections import deque
from math import lcm


class Solution(StrSplitSolution):
    _year = 2023
    _day = 20
    low_pulses, high_pulses, presses = 0, 0, 0

    def press(self, adj, conjs, ffs, rx_conj, rx_conj_presses):
        self.presses += 1

        self.low_pulses += 1 + len(adj["broadcaster"])
        queue = deque()
        for dest in adj["broadcaster"]:
            queue.append((0, "broadcaster", dest))

        while queue:
            pulse, src, label = queue.popleft()

            if label == "rx":
                continue

            # conjunction
            to_send = 0
            if label in conjs:
                conjs[label][src] = pulse
                if any(n == 0 for n in conjs[label].values()):
                    to_send = 1

            # flip-flop
            if label in ffs:
                if pulse == 1:
                    continue
                ffs[label] = not ffs[label]
                if ffs[label]:
                    to_send = 1

            # increment low or high pulses
            if to_send == 1:
                self.high_pulses += len(adj[label])
            else:
                self.low_pulses += len(adj[label])

            # send pulse to destination modules
            for dest in adj[label]:
                queue.append((to_send, label, dest))

            # check if any of the inputs connected to the conjunction
            # connected to "rx" are one and record the number of presses
            for label, val in conjs[rx_conj].items():
                if val == 1 and label not in rx_conj_presses:
                    rx_conj_presses[label] = self.presses

        return adj, conjs, ffs, rx_conj, rx_conj_presses

    @answer((819397964, 252667369442479))
    def solve(self) -> tuple[int, int]:

        adj = {}
        conjs = {}
        ffs = {}
        rx_conj_presses = {}
        rx_conj = ""

        for line in self.input:
            module, dests = line.split(" -> ")
            dests = dests.split(", ")
            t = module[0]
            if module == "broadcaster":
                adj["broadcaster"] = dests
            else:
                label = module[1:]
                adj[label] = dests

            if "rx" in dests:
                rx_conj = label

            if t == "&":
                conjs[label] = {}

            if t == "%":
                ffs[label] = False

        for label, dests in adj.items():
            for dest in dests:
                if dest in conjs:
                    conjs[dest][label] = 0

        for _ in range(1000):
            adj, conjs, ffs, rx_conj, rx_conj_presses = self.press(adj, conjs, ffs, rx_conj, rx_conj_presses)
        resPart1 = self.low_pulses * self.high_pulses

        while len(rx_conj_presses) < 4:
            adj, conjs, ffs, rx_conj, rx_conj_presses = self.press(adj, conjs, ffs, rx_conj, rx_conj_presses)

        return resPart1, lcm(*rx_conj_presses.values())
