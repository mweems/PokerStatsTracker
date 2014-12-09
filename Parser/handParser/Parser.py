from pyparsing import Word, Literal, nums, alphas, alphanums, OneOrMore, \
    Combine, Optional, Group

def handStartAmount(text):
    decimalNum = Combine(Word(nums, nums + ",") +
        Optional("." + OneOrMore(Word(nums))))
    seat = Group(Literal("Seat") + Word(nums) + Literal(":").suppress())
    player = Literal("mweems1")
    stack = Literal("(").suppress() + Literal("$").suppress()\
        + decimalNum + Literal(")").suppress()
    startAmount = seat + player + stack

    for line in text:
        start = startAmount.searchString(line)
        if len(start) > 0:
            return float(start[0][2])

    return None


def handEndAmount(text):
    return 0