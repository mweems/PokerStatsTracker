from pyparsing import Word, Literal, nums, alphas, alphanums, OneOrMore, \
    Combine, Optional, Group

num = Word(nums)
lett = Word(alphas)
date = Combine(num + "/" + num + "/" + num)
dollar = Literal("$").suppress()

decimalNum = Combine(Word(nums, nums + ",") +
                     Optional("." + OneOrMore(Word(nums))))



seat = Group(Literal("Seat") + Word(nums) + Literal(":").suppress())
me = Literal("mweems1")
stack = Literal("(").suppress() + Literal("$").suppress() \
    + decimalNum + Literal(")").suppress()
startAmount = seat + me + stack




id = Literal("#").suppress() + OneOrMore(Word(nums))

player = Group(Combine(OneOrMore(Word(alphanums)) +
                       Optional("-" + OneOrMore(Word(alphanums)))) +
               Optional(OneOrMore(Word(alphanums))))

stakes = dollar + decimalNum + Literal("/").suppress() + \
            dollar + decimalNum

seat = Literal("Seat") + num
stack = Literal("(").suppress() + dollar + decimalNum + Literal(")").suppress()
playerLocation = seat + Literal(":") + \
                 Group(Combine(OneOrMore(Word(alphanums)) +
                 Optional("-" + OneOrMore(Word(alphanums)))) +
                    Optional(OneOrMore(Word(alphanums)))).\
                        setResultsName("playerName") + stack

button = Literal('The button is in seat #').suppress() + num

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

flop = Literal("[").suppress() + Group(card + card + card) + \
       Literal("]").suppress()

flopPot = Group(Literal("*** FLOP ***") + flop +
                Literal("(Total Pot:")).suppress() + betAmount

turnPot = Group(Literal("*** TURN ***") + flop + Literal("[") + card +
                Literal("]") + Literal("(Total Pot:")).suppress() + betAmount

riverPot = Group(Literal("*** RIVER ***") + Literal('[') + card + card +
                 card + card + Literal("] [") + card + Literal("]") +
                 Literal("(Total Pot:")).suppress() + betAmount

turn = Literal("[").suppress() + card + Literal("]").suppress()

river = Group(Literal("[") + Group(card + card + card + card) +
              Literal("]")).suppress() + Literal("[") + card + Literal("]")

winningPlayer = player + Literal("(").suppress() + betAmount + \
                Literal(")").suppress()

winningHand = player + Literal("[").suppress() + card + card + \
              Literal("]").suppress()

mucked = Group(seat + Literal(":")).suppress() + player + hand

positionSummary = Group(seat + Literal(":")).suppress() + player + \
                  Group(Literal("(") + Group(OneOrMore(lett)) +
                        Literal(")")).suppress() + Group(OneOrMore(lett))

foldedPre = Group(seat + Literal(":")).suppress() + player

delimeterText = Literal("***").suppress() + OneOrMore(lett) + \
                Literal("***").suppress()