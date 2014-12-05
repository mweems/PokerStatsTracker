import helperMethods as helper
from pyparsing import Word, Literal, nums, OneOrMore, Combine, Optional


def firstLineParser(text):
    hand = {}

    id = Literal("#").suppress() + OneOrMore(Word(nums))
    found_id = id.searchString(text)[0][0]

    num = Word(nums)
    date = Combine(num + "/" + num + "/" + num)
    found_date = date.searchString(text)[0][0]

    decimalNum = Combine(Word(nums, nums+",") +
                         Optional("." + OneOrMore(Word(nums))))
    dollar = Literal("$").suppress()
    stakes = dollar + decimalNum + Literal("/").suppress() + \
                dollar + decimalNum
    found_stakes = stakes.searchString(text)

    hand['id'] = int(found_id)
    hand['date'] = helper._getDate(found_date)
    hand['stakes'] = helper._getStakes(found_stakes[0])

    return hand


def parsePlayers(text):
    players = {}
    splitText = text.split("Seat")
    splitText.pop(0)
    for line in splitText:
        newLine = line.replace(" ", "")
        player = helper._convertPlayerInfo(newLine)
        players.update(player)
    return players


def setLocations(text, players):
    splitText = text.split()
    button_index = helper._getUnique_number(splitText[-1])
    button = players[button_index]['name']
    locations = {
        "BTN": button,
        "SB": players[helper._checkIndex(button_index + 1)]['name'],
        "BB": players[helper._checkIndex(button_index + 2)]['name'],
        "UTG": players[helper._checkIndex(button_index + 3)]['name'],
        "MP": players[helper._checkIndex(button_index + 4)]['name'],
        "CO": players[helper._checkIndex(button_index + 5)]['name'],
    }
    return locations


def getHandValue(text):
    splitText = text.split("[")
    hands = splitText[1].split()
    hand = {
        "Card1": hands[0],
        "Card2": hands[1].strip(']')
    }
    return hand


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