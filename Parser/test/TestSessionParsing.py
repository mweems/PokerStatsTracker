import unittest
import Parser.sessionParser.parseSession as parser

class TestSessionParser(unittest.TestCase):
    text = open("Parser/test/TestSessionData.txt", "r").readlines()

    def testSessionHandSize(self):
        session = parser.parseSession(self.text)
        print session
        self.failUnlessEqual(1, 16)