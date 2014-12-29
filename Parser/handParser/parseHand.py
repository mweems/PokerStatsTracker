import Parser.textParser.quickLookParser as Parse


def getHand(text):
    hand = {}
    methods = [_getHandInfo, _getPlayers, _getButton]

    return hand

def _getHandInfo(line):
    try:
        hand = Parse.firstLineParser(line)
    except:
        hand = None
    if hand:
        return {"handInfo": hand}

def _getPlayers(text):
    playerList = []
    for line in text:
        try:
            players = Parse.parsePlayers(line)
        except:
            players = None
        if players:
            playerList.append(players)

    return {"players": playerList}

def _getButton(text):
    try:
        button = Parse.getButton(text)
    except:
        button = None
    if button:
        return button

def _getHoleCards(text):
    try:
        cards = Parse.getHandValue(text)
    except:
        cards = None
    if cards:
        return {"cards": cards}

def _preFlopAction(text):
    actions = []
    editedActions = []
    for line in text:
        try:
            action = Parse.checkAction(line)
        except:
            action = None
        if action:
            actions.append(action)
    for action in actions:
        print action
    return {"preFlopAction": actions}