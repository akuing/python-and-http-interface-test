import unittest
class TestAssert(unittest.TestCase):
    def testAssertIn(self):
        self.assertIn("aaa","aaab ass dddddd")
        self.assertIn("aa",["aa","a"])