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
player = seat + Literal(":") + Group(Combine(OneOrMore(Word(alphanums)) +
                 Optional("-" + OneOrMore(Word(alphanums)))) + \
                 Optional(OneOrMore(Word(alphanums)))).\
    setResultsName("playerName") + stack

button = Literal('#').suppress() + Word(nums)

hand = Literal("[").suppress() + Combine(num +lett) + Combine(num + lett) + \
        Literal("]")
