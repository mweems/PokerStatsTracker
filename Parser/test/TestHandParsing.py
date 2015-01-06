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
            {"mweems1": 2.0},
            {"11 Hammer 1199": 1.38},
            {"AAlex777718": 1.79}
        ],
        "button": 2,
        "cards": ["4c", "8h"],
        "preFlopAction": [
            {"11 Hammer 1199": ["folds", 0.0]},
            {"AAlex777718": ["folds", 0.0]},
            {"kookie4061": ["calls", 0.02]},
            {"sampik87": ["calls", 0.02]},
            {"Burda-sergey": ["calls", 0.01]},
            {"mweems1": ["checks", 0.0]}
        ],
        "flop": ["Kh", "Js", "9s"],
        "flopPotSize": .08,
        "flopAction": [
            {"Burda-sergey": ["checks", 0.0]},
            {"mweems1": ["checks", 0.0]},
            {"kookie4061": ["checks", 0.0]},
            {"sampik87": ["checks", 0.0]}
        ],
        "turn": "Ks",
        "turnPotSize": .08,
        "turnAction": [
            {"Burda-sergey": ["checks", 0.0]},
            {"mweems1": ["checks", 0.0]},
            {"kookie4061": ["checks", 0.0]},
            {"sampik87": ["bets", 0.02]},
            {"Burda-sergey": ["folds", 0.0]},
            {"mweems1": ["folds", 0.0]},
            {"kookie4061": ["calls", 0.02]}
        ],
        "river": "Kc",
        "riverPotSize": .12,
        "riverAction": [
            {"kookie4061": ["checks", 0.0]},
            {"sampik87": ["bets", 0.1]},
            {"kookie4061": ["calls", 0.1]}
        ],
        "winningInfo": {
            "player": "sampik87",
            "hand": ["Jc", "8d"],
            "handText": "a full house , Kings full of Jacks"
        },
        "wonPotSize": .31,
        "summary": [
            {"kookie4061": ["mucked", ["9d", "Ac"]]},
            {"sampik87": ["showed", "-"]},
            {"Burda-sergey": ["folded", "Turn"]},
            {"mweems1": ["folded", "Turn"]},
            {"11 Hammer 1199": ["folded", "-"]},
            {"AAlex777718": ["folded", "-"]}
        ]
    }

    def testHand(self):
        actual = helper._handInfo(self.text)
        expected = {
                'id': 34944298551,
                'date': datetime.date(2014, 11, 21),
                'stakes': {
                    'small_blind': .01,
                    'big_blind': .02
            }
        }
        self.failUnlessEqual(actual, expected)

    def testPlayers(self):
        actual = helper._players(self.text)
        expected = [
                       {"kookie4061": 8.51},
                       {"sampik87": 1.62},
                       {"Burda-sergey": 2.41},
                       {"mweems1": 2},
                       {"11 Hammer 1199": 1.38},
                       {"AAlex777718": 1.79}
                   ]
        self.failUnlessEqual(actual, expected)

    def testHoleCards(self):
        actual = helper._holeCards(self.text)
        self.failUnlessEqual(actual, ["4c", "8h"])

    def testButton(self):
        actual = helper._button(self.text)
        self.failUnlessEqual(actual, 2)

    def testPreFlopAction(self):
        actual = helper._preFlopAction(self.text)
        expected = [
                {"11 Hammer 1199": ["folds", 0.0]},
                {"AAlex777718": ["folds", 0.0]},
                {"kookie4061": ["calls", 0.02]},
                {"sampik87": ["calls", 0.02]},
                {"Burda-sergey": ["calls", 0.01]},
                {"mweems1": ["checks", 0.0]}
            ]
        self.failUnlessEqual(actual, expected)

    def testFlopAction(self):
        actual = helper._flopAction(self.text)
        expected = [
                {"Burda-sergey": ["checks", 0]},
                {"mweems1": ["checks", 0]},
                {"kookie4061": ["checks", 0]},
                {"sampik87": ["checks", 0]}
            ]
        self.failUnlessEqual(actual, expected)

    def testTurnAction(self):
        actual = helper._turnAction(self.text)
        expected = [
                {"Burda-sergey": ["checks", 0]},
                {"mweems1": ["checks", 0]},
                {"kookie4061": ["checks", 0]},
                {"sampik87": ["bets", 0.02]},
                {"Burda-sergey": ["folds", 0]},
                {"mweems1": ["folds", 0]},
                {"kookie4061": ["calls", 0.02]}
            ]
        self.failUnlessEqual(actual, expected)

    def testRiverAction(self):
        actual = helper._riverAction(self.text)
        expected = [
                {"kookie4061": ["checks", 0]},
                {"sampik87": ["bets", 0.10]},
                {"kookie4061": ["calls", 0.10]}
            ]
        self.failUnlessEqual(actual, expected)

    def testFlop(self):
        actual = helper._flop(self.text)
        self.failUnlessEqual(actual, ["Kh", "Js", "9s"])

    def testTurn(self):
        actual = helper._turn(self.text)
        self.failUnlessEqual(actual, "Ks")

    def testRiver(self):
        actual = helper._river(self.text)
        self.failUnlessEqual(actual, "Kc")

    def testFlopPotSize(self):
        actual = helper._flopPotSize(self.text)
        expected = .08
        self.failUnlessEqual(actual, expected)

    def testTurnPotSize(self):
        actual = helper._turnPotSize(self.text)
        expected = .08
        self.failUnlessEqual(actual, expected)

    def testRiverPotSize(self):
        actual = helper._riverPotSize(self.text)
        expected = .12
        self.failUnlessEqual(actual, expected)

    def testWinningInfo(self):
        actual = helper._winningInfo(self.text)
        expected = {
                "player": "sampik87",
                "hand": ["Jc", "8d"],
                "handText": "a full house , Kings full of Jacks"
        }
        self.failUnlessEqual(actual, expected)

    def testWinningPotSize(self):
        actual = helper._winningPotSize(self.text)
        expected = .31
        self.failUnlessEqual(actual, expected)

    def testSummary(self):
        actual = helper._summary(self.text)
        expected = [
                {"kookie4061": ["mucked", ["9d", "Ac"]]},
                {"sampik87": ["showed", "-"]},
                {"Burda-sergey": ["folded", "Turn"]},
                {"mweems1": ["folded", "Turn"]},
                {"11 Hammer 1199": ["folded", "-"]},
                {"AAlex777718": ["folded", "-"]}
            ]
        self.failUnlessEqual(actual, expected)

    def testDataStructure(self):
        actual = getHand(self.text)
        expected = self.expected
        self.failUnlessEqual(actual['handInfo'], expected['handInfo'])
        self.failUnlessEqual(actual['players'], expected['players'])
        self.failUnlessEqual(actual['button'], expected['button'])
        self.failUnlessEqual(actual['cards'], expected['cards'])
        self.failUnlessEqual(actual['preFlopAction'], expected['preFlopAction'])
        self.failUnlessEqual(actual['flop'], expected['flop'])
        self.failUnlessEqual(actual['flopPotSize'], expected['flopPotSize'])
        self.failUnlessEqual(actual['flopAction'], expected['flopAction'])
        self.failUnlessEqual(actual['turn'], expected['turn'])
        self.failUnlessEqual(actual['turnPotSize'], expected['turnPotSize'])
        self.failUnlessEqual(actual['turnAction'], expected['turnAction'])
        self.failUnlessEqual(actual['river'], expected['river'])
        self.failUnlessEqual(actual['riverPotSize'], expected['riverPotSize'])
        self.failUnlessEqual(actual['riverAction'], expected['riverAction'])
        self.failUnlessEqual(actual['winningInfo'], expected['winningInfo'])
        self.failUnlessEqual(actual['wonPotSize'], expected['wonPotSize'])
        self.failUnlessEqual(actual['summary'], expected['summary'])
        self.failUnlessEqual(actual, self.expected)


if __name__ == '__main__':
    unittest.main()