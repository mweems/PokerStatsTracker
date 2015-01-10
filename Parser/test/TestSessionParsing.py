import unittest
import Parser.sessionParser.parseSession as parser

class TestMultipleSessionParsing(unittest.TestCase):

    def testMultipleSessions(self):
        sessions = ["Parser/test/text/TestSessionData.txt",
                    "Parser/test/text/SessionTwo.txt"]
        hands = parser.getMultipleSessions(sessions)


        self.failUnlessEqual(len(hands), 2)
        self.failUnlessEqual(len(hands[1]), 12)
        self.failUnlessEqual(len(hands[0]), 16)


class TestSessionParser(unittest.TestCase):
    text = open("Parser/test/text/TestSessionData.txt", "r").readlines()

    def testSession(self):
        actual = parser.getSession(self.text)
        self.failUnlessEqual(len(actual), 16)

if __name__ == '__main__':
    unittest.main()