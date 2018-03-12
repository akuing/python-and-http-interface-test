from MyCalcultor import MyCalculator
import unittest

class TestMyCalculatorByList(unittest.TestCase):

    testDataList = [
    {
        "name": "两个都是整数，且能够被整除的情况下结果正常",
        "param1": 8,
        "param2": 2,
        "expect": 4
    },
    {
        "name": "两个都是整数，且不能被整除的情况下结果为整数部分",
        "param1": 9,
        "param2": 2,
        "expect": 4
    },
    {
        "name": "两个输入参数为可以转换为整数的字符串，能够正常处理",
        "param1": "9",
        "param2": "2",
        "expect": 4
    },
    {
        "name": "两个输入参数为不能转换为整数的字符串，返回错误信息",
        "param1": "9.8",
        "param2": "2.1",
        "expect": "请输入正确的参数，参数必须是整数型或者可以转换为整数型的字符串"
    },
    {
        "name": "两个输入参数为不是整数的数字型，返回错误信息",
        "param1": 9.8,
        "param2": 2.1,
        "expect": "请输入正确的参数，参数必须是整数型或者可以转换为整数型的字符串"
    },
    {
        "name": "除数为零的时候，返回错误信息",
        "param1": 9,
        "param2": 0,
        "expect": "除数不能为零"
    },
    {
        "name": "两个输入参数为不是数字的字符串，返回错误信息",
        "param1": "ssd",
        "param2": "dd",
        "expect": "请输入正确的参数，参数必须是整数型或者可以转换为整数型的字符串"
    },
    {
        "name": "一个输入参数为不是数字的字符串，返回错误信息",
        "param1": "ssd",
        "param2": "11",
        "expect": "请输入正确的参数，参数必须是整数型或者可以转换为整数型的字符串"
    },
    {
        "name": "参数不是整型也不是字符串，返回错误信息",
        "param1": {"as": "value"},
        "param2": [11, 2, 2],
        "expect": "请输入正确的参数，参数必须是整数型或者可以转换为整数型的字符串"
    }
]

    def testRunTests(self):
        calc = MyCalculator()
        for testdata in self.testDataList:
            with self.subTest(msg=testdata["name"]):
                self.assertEqual(testdata["expect"],calc.divide(testdata["param1"],testdata["param2"]))
