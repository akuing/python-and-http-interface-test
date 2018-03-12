class Test:
    def methodA(self):
        print("这个方法是methodA")
        pass


def add(num1, num2):
    return "{0} + {1} = {2}".format(num1, num2, num1 + num2)


if (__name__ == "__main__"):
    if ("1 + 2 = 3" == add(1, 2)):
        print("测试通过")
    else:
        print("测试不通过")