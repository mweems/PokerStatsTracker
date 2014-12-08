import helperMethods as helper
import parserElements as parse


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
    seatInfo = parse.seat.searchString(text)
    player = parse.playerLocation.parseString(text)
    stack = parse.stack.searchString(text)[0][0]


    playerInfo = {
        "Seat": int(seatInfo[0][1]),
        "name": " ".join(player.playerName),
        "stack": float(stack)
    }
    return playerInfo


def setButton(text):
    seat = parse.button.searchString(text)[0][0]
    return {"Button": int(seat)}


def getHandValue(text):
    hands = parse.hand.searchString(text)[0]
    holeCards = {
        "Card1": hands[0],
        "Card2": hands[1]
    }
    return holeCards


def checkAction(text):
    player = parse.player.searchString(text)[0][0]
    action = player.pop(-1)
    if action == "to":
        action = player.pop(-1)
    amount = parse.betAmount.searchString(text)
    if amount:
        return {
            " ".join(player): action,
            "amount": float(amount[0][0])
        }
    return {
        " ".join(player): action
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
    winner = parse.winningPlayer.parseString(text)
    winner.playerName.pop(-1)
    return {
            "player": " ".join(winner.playerName),
            "hand": [winner.hand[0], winner.hand[1]],
            "handText": " ".join(winner.handText)
    }