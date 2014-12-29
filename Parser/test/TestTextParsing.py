import unittest
import datetime

from Parser.textParser.quickLookParser import firstLineParser, parsePlayers, \
    getButton, getHandValue, checkAction, getFlop, getPotSize, getNextCard,\
    getWinningPlayer, getWinningPot, getMuckedCards, delimeterText


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
        expected1 = {"kookie4061": 8.51}
        player2 = parsePlayers(self.player3)
        expected2 = {"Burda-sergey": 2.41}
        player3 = parsePlayers(self.player5)
        expected3 = {"11 Hammer 1199": 1.38}
        self.failUnlessEqual(player1, expected1)
        self.failUnlessEqual(player2, expected2)
        self.failUnlessEqual(player3, expected3)


class TestButtonLocation(unittest.TestCase):
    text = "The button is in seat #2"

    def testPlayerSeatsAccurate(self):
        button = getButton(self.text)
        self.failUnlessEqual(button, {"Button": 2})


class TestParsingCards(unittest.TestCase):
    text = "Dealt to mweems1 [4c 8h]"

    def testCardsGetCreatedProperly(self):
        hand = getHandValue(self.text)
        self.failUnlessEqual(hand, ["4c", "8h"])

class TestStreetDelimeters(unittest.TestCase):
    flopText = "*** FLOP *** [Kh Js 9s] (Total Pot: $0.08, 4 Players)"
    turnText = "*** TURN *** [Kh Js 9s] [Ks] (Total Pot: $0.08, 4 Players)"
    riverText = "*** RIVER *** [Kh Js 9s Ks] [Kc] " \
                "(Total Pot: $0.12, 2 Players)"

    def testDelimeters(self):
        flop = delimeterText(self.flopText)
        turn = delimeterText(self.turnText)
        river = delimeterText(self.riverText)
        self.failUnlessEqual(flop, "***")
        self.failUnlessEqual(turn, "***")
        self.failUnlessEqual(river, "***")


class TestPreFlopAction(unittest.TestCase):
    foldText = "11 Hammer 1199 folds"
    checkText = "mweems1 checks"
    betText = "11 Hammer 1199 bets $0.02"
    raiseText = "kookie4061 raises to $0.10"
    callText = "sampik87 calls $0.10"


    def testPreflopAction(self):
        fold = checkAction(self.foldText)
        expectedFold = {
            "player": "11 Hammer 1199",
            "action": "folds"
        }
        check = checkAction(self.checkText)
        expectedCheck = {
            "player": "mweems1",
            "action": "checks"
        }
        call = checkAction(self.callText)
        expectedCall = {
            "player": "sampik87",
            "action": "calls",
            "amount": .10
        }
        raises = checkAction(self.raiseText)
        expectedRaise = {
            "player": "kookie4061",
            "action": "raises",
            "amount": .10
        }
        bet = checkAction(self.betText)
        expectedBet = {
            "player": "11 Hammer 1199",
            "action": "bets",
            "amount": .02
        }
        blank = checkAction("Dealt to mweems1 [4c 8h]")
        expectedBlank = {}

        self.failUnlessEqual(fold, expectedFold)
        self.failUnlessEqual(check, expectedCheck)
        self.failUnlessEqual(call, expectedCall)
        self.failUnlessEqual(raises, expectedRaise)
        self.failUnlessEqual(bet, expectedBet)
        self.failUnlessEqual(blank, expectedBlank)


class TestParsingFlop(unittest.TestCase):
    text = "*** FLOP *** [Kh Js 9s] (Total Pot: $0.08, 4 Players)"

    def testSetsHandsProperly(self):
        flop = getFlop(self.text)
        expectedFlop = ["Kh", "Js", "9s"]
        self.failUnlessEqual(flop, expectedFlop)

    def testParsesPotSizeOnFlop(self):
        potSize = getPotSize(self.text)
        expected = {"potSize": .08}
        self.failUnlessEqual(potSize, expected)


class TestParsingTurn(unittest.TestCase):
    text = "*** TURN *** [Kh Js 9s] [Ks] (Total Pot: $0.08, 4 Players)"

    def testAddsTurnCardToBoard(self):
        cards = ["Kh", "Js", "9s"]
        board = getNextCard(self.text, cards)
        expected = ["Kh", "Js", "9s", "Ks"]
        self.failUnlessEqual(board, expected)

    def testParsesPotSizeOnTurn(self):
        potSize = getPotSize(self.text)
        expected = {"potSize": .08}
        self.failUnlessEqual(potSize, expected)


class TestParsingRiver(unittest.TestCase):
    text = "*** RIVER *** [Kh Js 9s Ks] [Kc] (Total Pot: $0.12, 2 Players)"

    def testAddsRiverCardToBoard(self):
        cards = ["Kh", "Js", "9s", "Ks"]
        board = getNextCard(self.text, cards)
        expected = ["Kh", "Js", "9s", "Ks", "Kc"]
        self.failUnlessEqual(board, expected)

    def testParsesPotSizeOnRiver(self):
        potSize = getPotSize(self.text)
        expected = {"potSize": .12}
        self.failUnlessEqual(potSize, expected)


class TestParsingWinningPlayerAndHand(unittest.TestCase):
    text = "sampik87 shows [Jc 8d] a full house, Kings full of Jacks"

    def testGetsWinningPlayer(self):
        player = getWinningPlayer(self.text)
        expected = {
            "player": "sampik87",
            "hand": ["Jc", "8d"],
            "handText": "a full house , Kings full of Jacks"
        }
        self.failUnlessEqual(player, expected)


class TestParsingWinningPotAmount(unittest.TestCase):
    text = "sampik87 wins the pot ($0.31)"

    def testGetWinningPot(self):
        pot = getWinningPot(self.text)
        expected = {
            "pot": .31
        }
        self.failUnlessEqual(pot, expected)

class TestSummaryInfo(unittest.TestCase):
    text = "Seat 1: kookie4061 mucked [9d Ac] - "
    "a full house, Kings full of Nines",

    def testGetMuckedCards(self):
        cards = getMuckedCards(self.text)
        expected = {
            "player": "kookie4061",
            "hand": ["9d", "Ac"]
        }
        self.failUnlessEqual(cards, expected)

if __name__ == '__main__':
    unittest.main()