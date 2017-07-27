class MyCalculator:
    def add(self,num1, num2):
        return "{0} + {1} = {2}".format(num1, num2, num1 + num2)

    def minus(self,num1, num2):
        return "{0} - {1} = {2}".format(num1, num2, num1 - num2)

    def multiply(self,num1, num2):
        return "{0} * {1} = {2}".format(num1, num2, num1 * num2)

    def divide(self,num1, num2):
        return "{0} ÷ {1} = {2}".format(num1, num2, num1 / num2)
