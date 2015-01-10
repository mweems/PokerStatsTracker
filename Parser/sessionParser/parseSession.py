import Parser.handParser.parseHand as handParser


def getMultipleSessions(sessions):
    hands = []
    for session in sessions:
        text = open(session, "r").readlines()
        actual = getSession(text)
        hands.append(actual)

    return hands


def getSession(text):
    session = []
    handList = []
    hand = []
    for line in text:
        if len(line) <= 1:
            expected = handParser.getHand(hand)
            handList.append(expected)
            hand = []
        hand.append(str(line))
    for hand in handList:
        if hand['handInfo']:
            session.append(hand)
    return session

