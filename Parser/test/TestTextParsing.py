import unittest
import datetime

from Parser.textParser.Parser import firstLineParser, parsePlayers, \
    setButton, getHandValue, checkFold, checkCall, checkBet, checkRaise, \
    getFlop, getPotSize, getPlayers, getTurn, getRiver, getWinningPlayer


class TestParsingFirstLine(unittest.TestCase):
    firstLine = "Full Tilt Poker Game #34944298551: " \
                "Table Ard (New to the Game, 6 max) " \
                "- NL Hold'em - $0.01/$0.02 - 08:42:02 ET - 2014/11/21"

    def testGetsUniqueIdentitfyer(self):
        hand = firstLineParser(self.firstLine)

        self.failUnlessEqual(hand['id'], 34944298551)

    def testGetsDate(self):
        hand = firstLineParser(self.firstLine)

        self.failUnlessEqual(hand['date'], datetime.date(2014, 11, 21))

    def testGetsStakes(self):
        hand = firstLineParser(self.firstLine)
        stakes = hand['stakes']
        self.failUnlessEqual(stakes['small_blind'], .01)
        self.failUnlessEqual(stakes['big_blind'], .02)


class TestParsingPreflop(unittest.TestCase):
    player1 = "Seat 1: kookie4061 ($8.51)"
    player2 = "Seat 2: sampik87 ($1.62)"
    player3 = "Seat 3: Burda-sergey ($2.41)"
    player4 = "Seat 4: mweems1 ($2)"
    player5 = "Seat 5: 11 Hammer 1199 ($1.38)"
    player6 = "Seat 6: AAlex777718 ($1.79)"

    def testPlayerMatchesMoneyAndSeat(self):
        player1 = parsePlayers(self.player1)
        expected1 = {
            "Seat": 1,
            "name": "kookie4061",
            "stack": 8.51
        }
        player2 = parsePlayers(self.player3)
        expected2 = {
            "Seat": 3,
            "name": "Burda-sergey",
            "stack": 2.41
        }
        player3 = parsePlayers(self.player5)
        expected3 = {
            "Seat": 5,
            "name": "11 Hammer 1199",
            "stack": 1.38
        }
        self.failUnlessEqual(player1, expected1)
        self.failUnlessEqual(player2, expected2)
        self.failUnlessEqual(player3, expected3)


class TestButtonLocation(unittest.TestCase):
    text = "The button is in seat #2"

    def testPlayerSeatsAccurate(self):
        button = setButton(self.text)
        self.failUnlessEqual(button, {"Button": 2})


class TestParsingCards(unittest.TestCase):
    text = "Dealt to mweems1 [4c 8h]"

    def testCardsGetCreatedProperly(self):
        hand = getHandValue(self.text)
        self.failUnlessEqual(hand, {"Card1": "4c", "Card2": "8h"})


class TestPreFlopAction(unittest.TestCase):
    text = "11 Hammer 1199 folds " \
           "AAlex777718 folds " \
           "kookie4061 calls $0.02 " \
           "sampik87 calls $0.02 " \
           "Burda-sergey calls $0.01 " \
           "mweems1 checks"

    otherText = "11 Hammer 1199 bets $0.02 " \
                "AAlex777718 folds " \
                "kookie4061 raises to $0.10 " \
                "sampik87 calls $0.10 " \
                "Burda-sergey folds " \
                "mweems1 folds " \
                "11 Hammer 1199 folds"

    stakes = {
        "smallBlind": .01,
        "bigBlind": .02
    }

    def testCheckIfFolded(self):
        pre = checkFold(self.text)
        foldedPre = [
            "1199",
            "AAlex777718"
        ]
        self.failUnlessEqual(pre, foldedPre)

    def testCheckIfCalled(self):
        pre = checkCall(self.text, self.stakes)
        callPre = {
            "kookie4061": .02,
            "sampik87": .02,
            "Burda-sergey": .02,
            "mweems1": .02}

        self.failUnlessEqual(pre['kookie4061'], callPre['kookie4061'])

    def testCheckIfBet(self):
        pre = checkBet(self.otherText)
        betPre = {"1199": .02}
        self.failUnlessEqual(pre, betPre)

    def testCheckIfRaises(self):
        pre = checkRaise(self.otherText)
        raisePre = {"kookie4061": .10}
        self.failUnlessEqual(pre, raisePre)


class TestParsingFlop(unittest.TestCase):
    text = "*** FLOP *** [Kh Js 9s] (Total Pot: $0.08, 4 Players)"

    def testSetsHandsProperly(self):
        flop = getFlop(self.text)
        expectedFlop = ["Kh", "Js", "9s"]
        self.failUnlessEqual(flop, expectedFlop)

    def testParsesPotSizeOnFlop(self):
        potSize = getPotSize(self.text, "flop")
        expected = .08
        self.failUnlessEqual(potSize, expected)

    def testNumPlayersOnFlop(self):
        numPlayer = getPlayers(self.text, "flop")
        expected = 4
        self.failUnlessEqual(numPlayer, expected)


class TestParsingTurn(unittest.TestCase):
    text = "*** TURN *** [Kh Js 9s] [Ks] (Total Pot: $0.08, 4 Players)"

    def testAddsTurnCardToBoard(self):
        cards = ["Kh", "Js", "9s"]
        board = getTurn(self.text, cards)
        expected = ["Kh", "Js", "9s", "Ks"]
        self.failUnlessEqual(board, expected)

    def testParsesPotSizeOnTurn(self):
        potSize = getPotSize(self.text, "turn")
        expected = .08
        self.failUnlessEqual(potSize, expected)

    def testNumPlayersOnTurn(self):
        numPlayer = getPlayers(self.text, "turn")
        expected = 4
        self.failUnlessEqual(numPlayer, expected)


class TestParsingRiver(unittest.TestCase):
    text = "*** RIVER *** [Kh Js 9s Ks] [Kc] (Total Pot: $0.12, 2 Players)"

    def testAddsRiverCardToBoard(self):
        cards = ["Kh", "Js", "9s", "Ks"]
        board = getRiver(self.text, cards)
        expected = ["Kh", "Js", "9s", "Ks", "Kc"]
        self.failUnlessEqual(board, expected)

    def testParsesPotSizeOnRiver(self):
        potSize = getPotSize(self.text, "river")
        expected = .12
        self.failUnlessEqual(potSize, expected)

    def testNumPlayersOnriver(self):
        numPlayer = getPlayers(self.text, "river")
        expected = 2
        self.failUnlessEqual(numPlayer, expected)


class TestParsingWinner(unittest.TestCase):
    text = "sampik87 shows [Jc 8d] a full house, Kings full of Jacks " \
           "kookie4061 mucks " \
           "sampik87 wins the pot ($0.31) " \
           "with a full house, Kings full of Jacks"

    def testGetsWinningPlayer(self):
        player = getWinningPlayer(self.text)
        expected = {
            "sampik87": {
                "hand": ["Jc", "8d"],
                "pot": .31
            }
        }
        self.failUnlessEqual(player, expected)


if __name__ == '__main__':
    unittest.main()