import unittest
import datetime
from Parser.handParser.parseHand import getHand
from Parser.handParser import parseHand as helper


class TestHandParser(unittest.TestCase):
    text = open("Parser/test/TestHandData.txt", "r").readlines()
    expected = {
        "handInfo": {
            'id': 34944298551,
            'date': datetime.date(2014, 11, 21),
            'stakes': {
                'small_blind': .01,
                'big_blind': .02
            }
        },
        "players": [
            {"kookie4061": 8.51},
            {"sampik87": 1.62},
            {"Burda-sergey": 2.41},
            {"mweems1": 2},
            {"11 Hammer 1199": 1.38},
            {"AAlex777718": 1.79}
        ],
        "button": 2,
        "cards": ["4c", "8h"],
        "preFlopAction": {
            "11 Hammer 1199": {"folds", 0},
            "AAlex777718": {"folds", 0},
            "kookie4061": {"calls", 0.02},
            "sampik87": {"calls", 0.02},
            "Burda-sergey": {"calls", 0.01},
            "mweems1": {"checks", 0}
        },
        "flop": ["Kh", "Js", "9s"],
        "flopPotSize": .08,
        "flopAction": {
            "Burda-sergey": {"checks", 0},
            "mweems1": {"checks", 0},
            "kookie4061": {"checks", 0},
            "sampik87": {"checks", 0}
        },
        "turn": ["Kh", "Js", "9s", "Ks"],
        "turnPotSize": .08,
        "turnAction": {
            "Burda-sergey": {"checks", 0},
            "mweems1": {"checks", 0},
            "kookie4061": {"checks", 0},
            "sampik87": {"bets", 0.02},
            "Burda-sergey": {"folds", 0},
            "mweems1": {"folds", 0},
            "kookie4061": {"calls", 0.02}
        },
        "river": ["Kh", "Js", "9s", "Ks", "Kc"],
        "riverPotSize": .12,
        "riverAction": {
            "kookie4061": {"checks", 0},
            "sampik87": {"bets": 0.10},
            "kookie4061": {"calls", 0.10}
        },
        "winningInfo": {
            "player": "sampik87",
            "hand": ["Jc", "8d"],
            "handText": "a full house , Kings full of Jacks"
        },
        "wonPotSize": .31,
        "muckedCards": {"kookie4061": ["9d", "Ac"]}
    }

    def testHand(self):
        actual = helper._getHandInfo(self.text)
        expected = {
            "handInfo": {
                'id': 34944298551,
                'date': datetime.date(2014, 11, 21),
                'stakes': {
                    'small_blind': .01,
                    'big_blind': .02
                }
            }
        }
        self.failUnlessEqual(actual, expected)

    def testPlayers(self):
        actual = helper._getPlayers(self.text)
        expected = {
            "players": [
                       {"kookie4061": 8.51},
                       {"sampik87": 1.62},
                       {"Burda-sergey": 2.41},
                       {"mweems1": 2},
                       {"11 Hammer 1199": 1.38},
                       {"AAlex777718": 1.79}
                   ]}
        self.failUnlessEqual(actual, expected)

    def testHoleCards(self):
        actual = helper._getHoleCards(self.text)
        expected = {"cards": ["4c", "8h"]}
        self.failUnlessEqual(actual, expected)

    def testPreFlopAction(self):
        actual = helper._preFlopAction(self.text)
        expected = {
            "preFlopAction": {
                "11 Hammer 1199": {"folds", 0},
                "AAlex777718": {"folds", 0},
                "kookie4061": {"calls", 0.02},
                "sampik87": {"calls", 0.02},
                "Burda-sergey": {"calls", 0.01},
                "mweems1": {"checks", 0}
            }
        }
        self.failUnlessEqual(actual, expected)

    # def testDataStructure(self):
    #     actual = getHand(self.text)
    #     self.failUnlessEqual(actual, self.expected)


if __name__ == '__main__':
    unittest.main()