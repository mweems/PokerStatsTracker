import datetime


def _get_date(text):
    date = text.split("/")
    return datetime.date(int(date[0]), int(date[1]), int(date[2]))


def _get_unique_number(text):
    id = text.strip('#').strip(":").strip("#")
    return int(id)


def _get_stakes(text):
    stakes = text.split("/")
    small = stakes[0].strip("$")
    big = stakes[1].strip("$")
    int_stakes = {
        "small_blind": float(small),
        "big_blind": float(big)
    }
    return int_stakes


def _to_value(text):
    if type(text) == float or type(text) == int:
        return text
    value = text.strip(")").strip("$").strip(",")
    return float(value)


def _convert_player_info(text):
    atNumber = text.split(":")
    info = atNumber[1].split("(")
    return {
        int(atNumber[0]): {
            "name": info[0],
            "stack": _to_value(info[1])
        }

    }


def _check_index(int):
    if int > 6:
        return 1
    else:
        return int


def _cardValue(text):
    value = text.strip("[").strip("]")
    return value


def _winningPlayer(text):
    splittext = text.split()
    player = ''
    for word in splittext:
        previousIndex = splittext.index(word) - 1
        if word == "wins":
            player = splittext[previousIndex]
    return player


def _winningHand(text):
    text1 = text.split("[")
    text2 = text1[1].split("]")
    cards = text2[0].split()
    return [_cardValue(cards[0]), _cardValue(cards[1])]


def _winningPot(text):
    text1 = text.split("(")
    text2 = text1[1].split(")")
    return _to_value(text2[0])


def firstLineParser(text):
    hand = {}
    splitText = text.split()

    hand['id'] = _get_unique_number(splitText[4])
    hand['date'] = _get_date(splitText[-1])
    hand['stakes'] = _get_stakes(splitText[-6])

    return hand


def parsePlayers(text):
    players = {}
    splitText = text.split("Seat")
    splitText.pop(0)
    for line in splitText:
        newLine = line.replace(" ", "")
        player = _convert_player_info(newLine)
        players.update(player)
    return players


def setLocations(text, players):
    splitText = text.split()
    button_index = _get_unique_number(splitText[-1])
    button = players[button_index]['name']
    locations = {
        "BTN": button,
        "SB": players[_check_index(button_index + 1)]['name'],
        "BB": players[_check_index(button_index + 2)]['name'],
        "UTG": players[_check_index(button_index + 3)]['name'],
        "MP": players[_check_index(button_index + 4)]['name'],
        "CO": players[_check_index(button_index + 5)]['name'],
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
                called[word] = _to_value(splittext[money])
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
            bet[splittext[previouIndex]] = _to_value(splittext[nextIndex])
    return bet


def checkRaise(text):
    splittext = text.split()
    raises = {}
    for word in splittext:
        previouIndex = splittext.index(word) - 1
        nextIndex = splittext.index(word) + 2
        if word == "raises":
            raises[splittext[previouIndex]] = _to_value(splittext[nextIndex])
    return raises


def getFlop(text):
    splittext = text.split()
    flop = [
        _cardValue(splittext[3]),
        splittext[4],
        _cardValue(splittext[5])
    ]
    return flop


def getPotSize(text, round):
    splittext = text.split()
    if round == 'flop':
        return _to_value(splittext[8])
    if round == 'turn':
        return _to_value(splittext[9])
    if round == 'river':
        return _to_value(splittext[10])


def getPlayers(text, round):
    splittext = text.split()
    if round == 'flop':
        return _get_unique_number(splittext[9])
    if round == 'turn':
        return _get_unique_number(splittext[10])
    if round == 'river':
        return _get_unique_number(splittext[11])


def getTurn(text, cards):
    splittext = text.split()
    cards.append(_cardValue(splittext[6]))
    return cards


def getRiver(text, cards):
    splittext = text.split()
    cards.append(_cardValue(splittext[7]))
    return cards


def getWinningPlayer(text):
    player = _winningPlayer(text)
    hand = _winningHand(text)
    pot = _winningPot(text)
    return {
        player: {
            "hand": hand,
            "pot": pot
        }
    }