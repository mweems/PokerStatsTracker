from pyparsing import Word, Literal, nums, alphas, alphanums, OneOrMore, \
    Combine, Optional, Group

id = Literal("#").suppress() + OneOrMore(Word(nums))

num = Word(nums)
lett = Word(alphas)
date = Combine(num + "/" + num + "/" + num)

decimalNum = Combine(Word(nums, nums + ",") +
                     Optional("." + OneOrMore(Word(nums))))
dollar = Literal("$").suppress()
stakes = dollar + decimalNum + Literal("/").suppress() + \
            dollar + decimalNum

seat = Literal("Seat") + num
stack = Literal("(").suppress() + dollar + decimalNum + Literal(")").suppress()
playerLocation = seat + Literal(":") + \
                 Group(Combine(OneOrMore(Word(alphanums)) +
                 Optional("-" + OneOrMore(Word(alphanums)))) +
                    Optional(OneOrMore(Word(alphanums)))).\
                        setResultsName("playerName") + stack

button = Literal('#').suppress() + num

set = Optional(Literal("A")) + Optional(Literal("K")) + \
      Optional(Literal("Q")) + Optional(Literal("J"))

card = Combine(Optional(set) + Optional(num) + lett)

hand = Literal("[").suppress() + card + card + Literal("]").suppress()


fold = Literal('folds')
call = Literal('calls')
bet = Literal('bets')
raises = Literal('raises')
check = Literal('checks')

literalAction = Optional(check) + Optional(bet) + Optional(fold) + \
                Optional(call) + Optional(raises)

action = literalAction

betAmount = dollar + decimalNum

player = Group(Combine(OneOrMore(Word(alphanums)) +
                       Optional("-" + OneOrMore(Word(alphanums)))) +
               Optional(OneOrMore(Word(alphanums)))).setResultsName(
    "playerName")

flop = Literal("[").suppress() + Group(card + card + card) + \
       Literal("]").suppress()

pot = dollar + decimalNum

turn = Literal("[").suppress() + card + Literal("]").suppress()

winningPlayer = player + hand.setResultsName("hand") + \
                Group(OneOrMore(lett) + Literal(",") +
                      (OneOrMore(lett))).setResultsName("handText")

winningPot = Literal("(").suppress() + dollar + decimalNum + \
             Literal(")").suppress()