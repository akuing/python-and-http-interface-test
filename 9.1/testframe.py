class TestFrame:
    def __init__(self):
        self.currentMethod =""
        pass
    def runTest(self):
        for methodname in dir(self):
            if (methodname[0:4] == "test"):
                method = getattr(self,methodname)
                self.currentMethod = methodname
                method()
        pass
    def testForExample(self):
        pass
    def assertEqual(self,object1,object2):
        if(object1 == object2):
            print(self.currentMethod + " 测试通过!")
        else:
            print(self.currentMethod + " 测试失败! 预期结果是： " + object1 + " ，实际结果是： " + object2)


if(__name__ == "__main__"):
    mytestcase = TestFrame()
    print(dir(mytestcase))
    for methodname in dir(mytestcase):
        if(methodname[0:4] == "test"):
            print(methodname)


