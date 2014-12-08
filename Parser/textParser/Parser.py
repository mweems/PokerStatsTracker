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


def getPotSize(text, round):
    splittext = text.split()
    if round == 'flop':
        return helper._toValue(splittext[8])
    if round == 'turn':
        return helper._toValue(splittext[9])
    if round == 'river':
        return helper._toValue(splittext[10])


def getPlayers(text, round):
    splittext = text.split()
    if round == 'flop':
        return helper._getUnique_number(splittext[9])
    if round == 'turn':
        return helper._getUnique_number(splittext[10])
    if round == 'river':
        return helper._getUnique_number(splittext[11])


def getTurn(text, cards):
    splittext = text.split()
    cards.append(helper._cardValue(splittext[6]))
    return cards


def getRiver(text, cards):
    splittext = text.split()
    cards.append(helper._cardValue(splittext[7]))
    return cards


def getWinningPlayer(text):
    player = helper._winningPlayer(text)
    hand = helper._winningHand(text)
    pot = helper._winningPot(text)
    return {
        player: {
            "hand": hand,
            "pot": pot
        }
    }