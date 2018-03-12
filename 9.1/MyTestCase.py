from testframe import *

def add(num1, num2):
    return "{0} + {1} = {2}".format(num1, num2, num1 + num2)

class MyTestCase(TestFrame):
    def testAdd(self):
        self.assertEqual("1 + 2 = 3",add(1,2))

    def testAdd2(self):
        self.assertEqual("1 + 2 = 3", add(1, 1))

if(__name__ == "__main__"):
    testcase = MyTestCase()
    testcase.runTest()