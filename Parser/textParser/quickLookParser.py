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
    return {"Button": int(seat)}


def getHandValue(text):
    hands = parse.hand.searchString(text)[0]
    holeCards = [hands[0], hands[1]]
    return holeCards


def getMuckedCards(text):
    cards = getHandValue(text)
    playerText = parse.player.searchString(text)
    player = playerText[1][0]
    player.pop(-1)
    return {
        "player": " ".join(player),
        "hand": [cards[0], cards[1]]
    }


def checkAction(text):
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


def getPotSize(text):
    pot = parse.pot.searchString(text)[0][0]
    return {"potSize": float(pot)}


def getNextCard(text, cards):
    turn = parse.turn.searchString(text)[0][0]
    cards.append(turn)
    board = cards
    return board


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
    return {
        "pot": float(pot[0][0])
    }