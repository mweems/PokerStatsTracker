from pyparsing import Word, Literal, nums, OneOrMore, Combine, Optional

id = Literal("#").suppress() + OneOrMore(Word(nums))

num = Word(nums)
date = Combine(num + "/" + num + "/" + num)

decimalNum = Combine(Word(nums, nums+",") +
                     Optional("." + OneOrMore(Word(nums))))
dollar = Literal("$").suppress()
stakes = dollar + decimalNum + Literal("/").suppress() + \
         dollar + decimalNum
