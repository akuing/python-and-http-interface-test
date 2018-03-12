class TestFrame:
    def __init__(self):
        pass
    def runTest(self):
        for methodname in dir(self):
            if (methodname[0:4] == "test"):
                print(methodname)
        pass
    def testForExample(self):
        pass


if(__name__ == "__main__"):
    mytestcase = TestFrame()
    print(dir(mytestcase))
    for methodname in dir(mytestcase):
        if(methodname[0:4] == "test"):
            print(methodname)


