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
    actions = _actions(text)
    preflop = []
    for playerAction in actions:
        try:
            list = playerAction[0]
            if list[0] == "FLOP":
                break
        except:
            player = playerAction['player']
            action = playerAction['action']
            amount = playerAction.get('amount')
            if not amount:
                amount = 0.0
            playerAction = {player: [action, amount]}
            preflop.append(playerAction)

    return {"preFlopAction": preflop}


def _flopAction(text):
    actions = _actions(text)
    preflop = _preFlopAction(text)["preFlopAction"]
    flop = []
    for playerAction in actions:
        try:
            list = playerAction[0]
            if list[0] == "TURN":
                break
        except:
            player = playerAction['player']
            action = playerAction['action']
            amount = playerAction.get('amount')
            if not amount:
                amount = 0.0
            playerAction = {player: [action, amount]}
            flop.append(playerAction)

    for action in preflop:
        flop.remove(action)
    return {"flopAction": flop}


def _turnAction(text):
    actions = _actions(text)
    preflop = _preFlopAction(text)["preFlopAction"]
    flop = _flopAction(text)["flopAction"]
    turn = []
    for playerAction in actions:
        try:
            list = playerAction[0]
            if list[0] == "RIVER":
                break
        except:
            player = playerAction['player']
            action = playerAction['action']
            amount = playerAction.get('amount')
            if not amount:
                amount = 0.0
            playerAction = {player: [action, amount]}
            turn.append(playerAction)

    for action in preflop:
        turn.remove(action)
    for action in flop:
        turn.remove(action)
    return {"turnAction": turn}


def _flop(text):
    try:
        flop = Parse.getFlop(text)
    except:
        flop = None
    if flop:
        return {"flop": flop}


def _turn(text):
    flop = _flop(text)
    try:
        turn = Parse.getTurn(text, flop['flop'])
    except:
        turn = None
    if turn:
        return {"turn": turn}


def _river(text):
    turn = _turn(text)
    for line in text:
        try:
            river = Parse.getRiver(line, turn['turn'])
        except:
            river = None

        if river:
            return {"river": river}


def _flopPotSize(text):
    try:
        pot = Parse.getFlopPotSize(text)
    except:
        pot = None
    if pot:
        return pot


def _turnPotSize(text):
    try:
        pot = Parse.getTurnPotSize(text)
    except:
        pot = None
    if pot:
        return pot


def _riverPotSize(text):
    try:
        pot = Parse.getRiverPotSize(text)
    except:
        pot = None
    if pot:
        return pot

def _actions(text):
    actions = []
    for line in text:
        try:
            action = Parse.checkAction(line)
        except:
            action = None
        if action:
            actions.append(action)
    return actions