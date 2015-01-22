import unittest
import datetime
from Parser.handParser.parseHand import getHand
from Parser.handParser import parseHand as helper
from Parser.testParser import ExpectedHandData as hand


class TestHandParser(unittest.TestCase):
    text1 = open("Parser/testParser/text/TestHandData.txt", "r").readlines()
    text2 = open("Parser/testParser/text/missingWinningInfo.txt", "r").readlines()
    text3 = open("Parser/testParser/text/missingInfo.txt", "r").readlines()
    text4 = open("Parser/testParser/text/underlineInUsername.txt", "r").readlines()

    expected2 = hand.missingWinningInfo
    expected1 = hand.firstHand
    expected3 = hand.infoMissing
    expected4 = hand.underscore

    def testHand(self):
        actual = helper._handInfo(self.text1)
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
        actual = helper._players(self.text1)
        expected = [
                       {"kookie4061": {
                           "seat": 1,
                           "stack": 8.51}},
                       {"sampik87": {
                           "seat": 2,
                           "stack": 1.62}},
                       {"Burda-sergey": {
                           "seat": 3,
                           "stack": 2.41}},
                       {"mweems1": {
                           "seat": 4,
                           "stack": 2}},
                       {"11 Hammer 1199": {
                           "seat": 5,
                           "stack": 1.38}},
                       {"AAlex777718": {
                           "seat": 6,
                           "stack": 1.79}}
                   ]
        self.failUnlessEqual(actual, expected)

    def testHoleCards(self):
        actual = helper._holeCards(self.text1)
        self.failUnlessEqual(actual, ["4c", "8h"])

    def testButton(self):
        actual = helper._button(self.text1)
        self.failUnlessEqual(actual, 2)

    def testPreFlopAction(self):
        actual = helper._preFlopAction(self.text1)
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
        actual = helper._flopAction(self.text1)
        expected = [
                {"Burda-sergey": ["checks", 0]},
                {"mweems1": ["checks", 0]},
                {"kookie4061": ["checks", 0]},
                {"sampik87": ["checks", 0]}
            ]
        self.failUnlessEqual(actual, expected)

    def testTurnAction(self):
        actual = helper._turnAction(self.text1)
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
        actual = helper._riverAction(self.text1)
        expected = [
                {"kookie4061": ["checks", 0]},
                {"sampik87": ["bets", 0.10]},
                {"kookie4061": ["calls", 0.10]}
            ]
        self.failUnlessEqual(actual, expected)

    def testFlop(self):
        actual = helper._flop(self.text1)
        self.failUnlessEqual(actual, ["Kh", "Js", "9s"])

    def testTurn(self):
        actual = helper._turn(self.text1)
        self.failUnlessEqual(actual, "Ks")

    def testRiver(self):
        actual = helper._river(self.text1)
        self.failUnlessEqual(actual, "Kc")

    def testFlopPotSize(self):
        actual = helper._flopPotSize(self.text1)
        expected = .08
        self.failUnlessEqual(actual, expected)

    def testTurnPotSize(self):
        actual = helper._turnPotSize(self.text1)
        expected = .08
        self.failUnlessEqual(actual, expected)

    def testRiverPotSize(self):
        actual = helper._riverPotSize(self.text1)
        expected = .12
        self.failUnlessEqual(actual, expected)

    def testWinningInfo(self):
        actual = helper._winningInfo(self.text1)
        expected = {
                "player": "sampik87",
                "wonPotSize": .31,
        }
        self.failUnlessEqual(actual, expected)

    def testWinningHand(self):
        actual = helper._winningHand(self.text1)
        expected = ["Jc", "8d"]
        self.failUnlessEqual(actual, expected)

    def testSummary(self):
        actual = helper._summary(self.text1)
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
        actual = getHand(self.text1)
        expected = self.expected1
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
        self.failUnlessEqual(actual['winningHand'], expected['winningHand'])
        self.failUnlessEqual(actual['summary'], expected['summary'])
        self.failUnlessEqual(actual, expected)

    def testDataStructure2(self):
        actual = getHand(self.text2)
        expected = self.expected2
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
        self.failUnlessEqual(actual['winningHand'], expected['winningHand'])
        self.failUnlessEqual(actual['summary'], expected['summary'])
        self.failUnlessEqual(actual, expected)

    def testDataStructure3(self):
        actual = getHand(self.text4)
        expected = self.expected4
        print "actual", actual['preFlopAction']
        print "expected", expected["preFlopAction"]
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
        self.failUnlessEqual(actual['winningHand'], expected['winningHand'])
        self.failUnlessEqual(actual['summary'], expected['summary'])
        self.failUnlessEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()