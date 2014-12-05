import datetime

def _getDate(text):
    date = text.split("/")
    return datetime.date(int(date[0]), int(date[1]), int(date[2]))


def _getUnique_number(text):
    id = text.strip('#').strip(":").strip("#")
    return int(id)


def _getStakes(text):
    int_stakes = {
        "small_blind": float(text[0]),
        "big_blind": float(text[1])
    }
    return int_stakes


def _toValue(text):
    if type(text) == float or type(text) == int:
        return text
    value = text.strip(")").strip("$").strip(",")
    return float(value)


def _convertPlayerInfo(text):
    atNumber = text.split(":")
    info = atNumber[1].split("(")
    return {
        int(atNumber[0]): {
            "name": info[0],
            "stack": _toValue(info[1])
        }

    }


def _checkIndex(int):
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
    return _toValue(text2[0])
