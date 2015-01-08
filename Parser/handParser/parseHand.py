import Parser.textParser.quickLookParser as Parse


def getHand(text):
    hand = {}
    hand['handInfo'] = _handInfo(text)
    hand['players'] = _players(text)
    hand['button'] = _button(text)
    hand['cards'] = _holeCards(text)
    hand['preFlopAction'] = _preFlopAction(text)
    hand['flop'] = _flop(text)
    hand['flopPotSize'] = _flopPotSize(text)
    hand['flopAction'] = _flopAction(text)
    hand['turn'] = _turn(text)
    hand['turnPotSize'] = _turnPotSize(text)
    hand['turnAction'] = _turnAction(text)
    hand['river'] = _river(text)
    hand['riverPotSize'] = _riverPotSize(text)
    hand['riverAction'] = _riverAction(text)
    hand['winningInfo'] = _winningInfo(text)
    hand['winningHand'] = _winningHand(text)
    hand['summary'] = _summary(text)
    return hand


def _handInfo(text):
    try:
        hand = Parse.firstLineParser(text)
    except:
        hand = None
    if hand:
        return hand


def _players(text):
    playerList = []
    for line in text:
        try:
            players = Parse.parsePlayers(line)
        except:
            players = None
        if players:
            playerList.append(players)

    return playerList


def _button(text):
    try:
        button = Parse.getButton(text)
    except:
        button = None
    if button:
        return button


def _holeCards(text):
    try:
        cards = Parse.getHandValue(text)
    except:
        cards = None
    if cards:
        return cards


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

    return preflop


def _flopAction(text):
    actions = _actions(text)
    preflop = _preFlopAction(text)
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
    return flop


def _turnAction(text):
    actions = _actions(text)
    preflop = _preFlopAction(text)
    flop = _flopAction(text)
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
    return turn


def _riverAction(text):
    actions = _actions(text)
    preflop = _preFlopAction(text)
    flop = _flopAction(text)
    turn = _turnAction(text)
    river = []
    for playerAction in actions:
        try:
            list = playerAction[0]
            if list[0] == "SHOW DOWN":
                break
        except:
            player = playerAction['player']
            action = playerAction['action']
            amount = playerAction.get('amount')
            if not amount:
                amount = 0.0
            playerAction = {player: [action, amount]}
            river.append(playerAction)
    for action in preflop:
        river.remove(action)
    for action in flop:
        river.remove(action)
    for action in turn:
        river.remove(action)
    return river


def _flop(text):
    try:
        flop = Parse.getFlop(text)
    except:
        flop = None
    if flop:
        return flop


def _turn(text):
    try:
        turn = Parse.getTurn(text)
    except:
        turn = None
    if turn:
        return turn


def _river(text):
    for line in text:
        try:
            river = Parse.getRiver(line)
        except:
            river = None

        if river:
            return river


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



def _winningInfo(text):
    try:
        winner = Parse.getWinningPlayer(text)
    except:
        winner = None
    if winner:
        return winner


def _winningHand(text):
    try:
        pot = Parse.getWinningHand(text)
    except:
        pot = None
    if pot:
        return pot
    return []


def _summary(text):
    summary = []
    for line in text:
        mucked = _getMuckedCards(line)
        positional = _getPositionSummary(line)
        foldedPre = _getFoldedPre(line)
        if mucked:
            summary.append(_setCards(mucked))
        if positional:
            summary.append(_setCards(positional))
        if foldedPre:
            summary.append(_setCards(foldedPre))

    return summary


def _setCards(text):
    info = text.get('info')
    if text['action'] == 'didn':
        text['action'] = 'folded'
    if not info:
        text['info'] = "-"
    return {text['player']: [text['action'], text['info']]}


def _getFoldedPre(text):
    try:
        folded = Parse.getFoldedPre(text)
    except:
        folded = None
    if folded:
        return folded


def _getPositionSummary(text):
    try:
        summary = Parse.getPositionSummary(text)
    except:
        summary = None
    if summary:
        return summary


def _getMuckedCards(text):
    try:
        mucked = Parse.getMucked(text)
    except:
        mucked = None
    if mucked:
        return mucked