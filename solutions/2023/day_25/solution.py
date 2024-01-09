# puzzle prompt: https://adventofcode.com/2023/day/25

from ...base import StrSplitSolution, answer
import networkx as nx
from math import prod


class Solution(StrSplitSolution):
    _year = 2023
    _day = 25

    @answer(601344)
    def part_1(self) -> int:
        graphDict = {}
        for i in self.input:
            key, vertices = i.split(": ")
            graphDict[key] = vertices.split(" ")
        G = nx.Graph(graphDict)
        for a, b in nx.minimum_edge_cut(G):
            G.remove_edge(a, b)
        part1 = prod(map(len, nx.connected_components(G)))
        return part1

    # @answer(1234)
    def part_2(self) -> int:
        pass
