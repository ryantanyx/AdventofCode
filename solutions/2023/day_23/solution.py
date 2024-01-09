# puzzle prompt: https://adventofcode.com/2023/day/23

from ...base import StrSplitSolution, answer
import networkx as nx
from networkx.classes.function import path_weight

class Solution(StrSplitSolution):
    _year = 2023
    _day = 23

    @answer((2154, 6654))
    def solve(self) -> tuple[int, int]:
        N, M = len(self.input), len(self.input[0])
        start, end = (0, 1), (N - 1, M - 2)

        prev = {">": (0, -1), "<": (0, 1), "^": (1, 0), "v": (-1, 0)}
        G1 = nx.grid_2d_graph(N, M, create_using=nx.DiGraph)
        G2 = nx.grid_2d_graph(N, M)
        for i, l in enumerate(self.input):
            for j, x in enumerate(l):
                p = (i, j)
                if x == "#":
                    G1.remove_node(p)
                    G2.remove_node(p)
                # allows for the assignment within the elif condition itself, assigning the result of prev.get(x)
                # to dp and checking its truthiness in one line.
                elif dp := prev.get(x):
                    di, dj = dp
                    G1.remove_edge(p, (i + di, j + dj))

        part1 = max(map(len, nx.all_simple_edge_paths(G1, start, end)))

        nodesWith2Edges = [node for node in G2.nodes if len(G2.edges(node)) == 2]

        # This for loop just contracts all the lines into 2 points,  eg - - - - becomes -- (with weight 4)
        for node in nodesWith2Edges:
            v1, v2 = list(G2.neighbors(node))
            # get the weight from the existing edge, else its 1. Then new weight = the sum of existing weights
            new_weight = sum(G2.edges[node, v].get("d", 1) for v in (v1, v2))
            G2.add_edge(v1, v2, d=new_weight)
            G2.remove_node(node)

        # iterates through all paths and find the associated weight (which is also the longest distance)
        part2 = max(path_weight(G2, path, "d") for path in nx.all_simple_paths(G2, start, end))

        return part1, part2
