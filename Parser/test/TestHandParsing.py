import unittest
from Parser.handParser.parseHand import handStartAmount, handEndAmount


class TestHandParser(unittest.TestCase):
    text = open("Parser/test/TestHandData.txt", "r").readlines()

    def testWonLostAmount(self):

        beginAmount = handStartAmount(self.text)
        endAmount = handEndAmount(self.text)
        # diff = beginAmount - endAmount

        self.failUnlessEqual(beginAmount, 2)
        self.failUnlessEqual(endAmount, 1.98)
        # self.failUnlessEqual(diff, -.02)

if __name__ == '__main__':
    unittest.main()