import unittest
import Parser.sessionParser.parseSession as parser


class TestSessionParser(unittest.TestCase):
    text = open("Parser/test/TestSessionData.txt", "r").readlines()

    def testSession(self):
        actual = parser.getSession(self.text)
        self.failUnlessEqual(len(actual), 16)

if __name__ == '__main__':
    unittest.main()