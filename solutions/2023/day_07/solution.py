# puzzle prompt: https://adventofcode.com/2023/day/7
import re

from ...base import StrSplitSolution, answer
from collections import Counter


class Solution(StrSplitSolution):
    _year = 2023
    _day = 7

    @answer(253933213)
    def part_1(self) -> int:
        store = ["A", "K", "Q", "J", "T", "9", "8", '7', '6', '5', '4', '3', '2']
        pointsDict = self.getInputs()
        cardsStore = self.splitHandsIntoGrps(pointsDict)
        combined = self.getCombinedOrderedHands(cardsStore, store)

        return self.calculateWinnings(combined, pointsDict)


    @answer(253473930)
    def part_2(self) -> int:
        store = ["A", "K", "Q", "T", "9", "8", '7', '6', '5', '4', '3', '2', "J"]
        pointsDict = self.getInputs()
        cardsStore = self.splitHandsIntoGrps(pointsDict, True)
        combined = self.getCombinedOrderedHands(cardsStore, store)

        return self.calculateWinnings(combined, pointsDict)

    def getInputs(self):
        res = []
        for i in self.input:
            res.append(re.findall("\w+", i))
        pointsDict = {}
        for j in res:
            pointsDict[j[0]] = int(j[1])
        return pointsDict

    def calculateWinnings(self, combined, pointsDict):
        res = 0
        for idx, i in enumerate(combined):
            res += (idx + 1) * pointsDict[i]
        return res

    def getCombinedOrderedHands(self, cardsStore, store):
        combined = []
        for cardList in cardsStore:
            cardList.sort(reverse=True, key=lambda x: (store.index(x[0]), store.index(x[1]),
                                                       store.index(x[2]), store.index(x[3]), store.index(x[4])))
            combined += cardList
        return combined

    def getUniqueLetterSet(self, cardDict, cardHand):
        if "J" in cardHand:
            # if the hand contains 'J', add the number of 'J' to the letter with the most number of cards in that hand
            numberOfJ = cardDict["J"]
            cardDict["J"] = 0
            highKey = None
            for letter, count in cardDict.items():
                if (highKey is None or count > cardDict[highKey]) and letter != "J":
                    highKey = letter
            cardDict[highKey] += numberOfJ
            uniqueLetters = set(cardDict.keys())
            uniqueLetters.remove("J")  # remove the letter J when determining the strength of the hand
        else:
            uniqueLetters = set(cardHand)
        return uniqueLetters

    def splitHandsIntoGrps(self, pointsDict, part2=False):
        # separate list for each hand strength, starting with (index number in brackets):
        # high card (0), one pair(1), two pair(2), three kind(3), house(4), four kind(5), five kind(6)
        cardsStore = [[] for i in range(7)]

        for i in pointsDict.keys():
            cardHand = Counter(i)
            uniqueLetters = set(i) if not part2 else self.getUniqueLetterSet(cardHand, i)
            if len(uniqueLetters) == 1:
                # only 1 unique card -> must be five of a kind
                cardsStore[6].append(i)
            elif len(uniqueLetters) == 5:
                # all are unique cards -> must be high card
                cardsStore[0].append(i)
            elif len(uniqueLetters) == 4:
                # 4 unique cards -> must be one pair
                cardsStore[1].append(i)
            else:
                for letter, count in cardHand.items():
                    if len(uniqueLetters) == 2:
                        if count == 3:
                            # 2 unique cards and there are 3 copies of 1 -> must be full house
                            cardsStore[4].append(i)
                            break
                        elif count == 4:
                            # 2 unique cards and there are 4 copies of 1 -> must be four of a kind
                            cardsStore[5].append(i)
                            break
                    if len(uniqueLetters) == 3:
                        if count == 3:
                            # 3 unique cards and there are 3 copies of 1 card -> must be three of a kind
                            cardsStore[3].append(i)
                            break
                        elif count == 2:
                            # 3 unique cards and there are 2 copies of 1 card -> must be 2 pairs
                            cardsStore[2].append(i)
                            break

        return cardsStore
