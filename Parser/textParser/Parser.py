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
    player = parse.player.parseString(text)
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


def checkFold(text):
    splittext = text.split()
    folded = []
    for word in splittext:
        nextIndex = splittext.index(word) + 1
        size = len(splittext)
        if nextIndex <= size - 1:
            if splittext[nextIndex] == "folds":
                folded.append(word)
    noDupes = []
    [noDupes.append(i) for i in folded if not noDupes.count(i)]

    return noDupes


def checkCall(text, stakes):
    splittext = text.split()
    called = {}
    for word in splittext:
        nextIndex = splittext.index(word) + 1
        money = splittext.index(word) + 2
        size = len(splittext)
        if money <= size - 1:
            if splittext[nextIndex] == "calls":
                called[word] = helper._toValue(splittext[money])
            if splittext[nextIndex] == "checks":
                called[word] = stakes['bigBlind']

    return called


def checkBet(text):
    splittext = text.split()
    bet = {}
    for word in splittext:
        previouIndex = splittext.index(word) - 1
        nextIndex = splittext.index(word) + 1
        if word == "bets":
            bet[splittext[previouIndex]] = helper._toValue(splittext[nextIndex])
    return bet


def checkRaise(text):
    splittext = text.split()
    raises = {}
    for word in splittext:
        previouIndex = splittext.index(word) - 1
        nextIndex = splittext.index(word) + 2
        if word == "raises":
            raises[splittext[previouIndex]] = helper._toValue(splittext[nextIndex])
    return raises


def getFlop(text):
    splittext = text.split()
    flop = [
        helper._cardValue(splittext[3]),
        splittext[4],
        helper._cardValue(splittext[5])
    ]
    return flop


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