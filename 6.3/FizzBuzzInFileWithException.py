class FizzBuzz:
    def getFizzBuzz(self,number):
        try:
            number = int(number.strip())
        except(ValueError):
            return "Exception\n"
        if (number % 3 == 0 and number % 5 == 0):
            return "FizzBuzz\n"

        elif (number % 3 == 0):
            return "Fizz\n"
        elif (number % 5 == 0):
            return "Buzz\n"
        else:
            return str(number)+"\n"

if(__name__ == "__main__"):
    inputFile = open("input.txt","r")
    outputFile = open("output.txt","w")
    fizzBuzz = FizzBuzz()
    for line in inputFile:
        outputStr = fizzBuzz.getFizzBuzz(line)
        outputFile.write(outputStr)
    inputFile.close()
    outputFile.close()
