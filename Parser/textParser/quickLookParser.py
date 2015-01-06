from Parser.helper import helperMethods as helper
from Parser.helper import parserElements as parse

Actions = ["checks", "calls", "raises", "bets", "folds"]

def _notLegal(action):
    if Actions.__contains__(action):
        return False
    return True

def firstLineParser(text):
    hand = {}
    found_id = parse.id.searchString(text)[0][0]
    found_date = parse.date.searchString(text)[0][0]
    found_stakes = parse.stakes.searchString(text)[0]

    hand['id'] = int(found_id)
    hand['date'] = helper._getDate(found_date)
    hand['stakes'] = helper._getStakes(found_stakes)

    return hand


def parsePlayers(text):
    player = parse.playerLocation.searchString(text)
    stack = parse.stack.searchString(text)[0][0]
    playerInfo = {
        " ".join(player[0][3]): float(stack)
    }
    return playerInfo


def getButton(text):
    seat = parse.button.searchString(text)[0][0]
    return int(seat)


def getHandValue(text):
    hands = parse.hand.searchString(text)[0]
    holeCards = [hands[0], hands[1]]
    return holeCards


def getMucked(text):
    mucked = parse.mucked.searchString(text)
    if mucked:
        cards = mucked[0]
        player = mucked[0][0]
        action = player.pop(-1)
        return {
            "player": " ".join(player),
            "action": action,
            "info": [cards[1], cards[2]]
        }
    return []
def getPositionSummary(text):
    summary = parse.positionSummary.searchString(text)
    if summary:
        player = summary[0][0]
        action = summary[0][1][0]
        return {
            "player": " ".join(player),
            "action": action,
            "info": _getInfo(summary[0][1])
        }
    return []
def _getInfo(list):
    if len(list) > 1:
        return list.pop(-1)
    return None

def getFoldedPre(text):
    summary = parse.foldedPre.searchString(text)
    action = summary[0][0].pop(-1)
    player = summary[0][0]
    if action == "didn":
        return {
            "player": " ".join(player),
            "action": action
        }
    return []


def checkAction(text):
    delimeter = parse.delimeterText.searchString(text)
    if delimeter:
        return delimeter
    player = parse.player.searchString(text)[0][0]
    action = player.pop(-1)
    if action == "to":
        action = player.pop(-1)
    if _notLegal(action):
        return {}
    amount = parse.betAmount.searchString(text)
    if amount:
        return {
            "player": " ".join(player),
            "action": action,
            "amount": float(amount[0][0])
        }
    return {
        "player": " ".join(player),
        "action": action
    }


def getFlop(text):
    flop = parse.flop.searchString(text)[0][0]
    return [flop[0], flop[1], flop[2]]


def getFlopPotSize(text):
    pot = parse.flopPot.searchString(text)[0][0]
    return float(pot)


def getTurnPotSize(text):
    pot = parse.turnPot.searchString(text)[0][0]
    return float(pot)


def getRiverPotSize(text):
    pot = parse.riverPot.searchString(text)[0][0]
    return float(pot)


def getTurn(text):
    turn = parse.turn.searchString(text)[0][0]
    return turn


def getRiver(text):
    river = parse.river.searchString(text)
    return river[0][1]


def getWinningPlayer(text):
    winner = parse.winningPlayer.searchString(text)
    winner[0][0].pop()
    player = winner[0][0]
    return {
        "player": " ".join(player),
        "hand": [winner[0][1], winner[0][2]],
        "handText": " ".join(winner[0][3])
    }


def getWinningPot(text):
    pot = parse.winningPot.searchString(text)
    wonPot = float(pot[0][0]) - float(pot[0][1])
    return wonPot

def delimeterText(text):
    text = parse.delimeterText.searchString(text)[0]
    return text[0]
