from Parser.helper import parserElements as parser


def handStartAmount(text):
    for line in text:
        start = parser.startAmount.searchString(line)
        if len(start) > 0:
            return float(start[0][2])

    return None


def handEndAmount(text):
    return 0