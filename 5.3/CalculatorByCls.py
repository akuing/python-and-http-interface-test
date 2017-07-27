from MyCalculator import *

operator = input('''选择运算符:
1 is +
2 is -
3 is x
4 is ÷
输入你的选择（1/2/3/4）:
''')
if(int(operator)<1 or int(operator)>4):
    print("这不是一个合法的运算符")
num1 = int(input("请输入第一个数："))
num2 = int(input("请输入第二个数："))
calc = MyCalculator()
if(operator == "1"):
    print(calc.add(num1,num2))
if(operator == "2"):
    print(calc.minus(num1,num2))
if(operator == "3"):
    print(calc.multiply(num1,num2))
if(operator == "4"):
    print(calc.divide(num1,num2))