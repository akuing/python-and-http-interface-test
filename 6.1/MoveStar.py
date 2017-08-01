from random import randint
import os
class Star:
    def __init__(self):
        self.position = randint(0,23)
    def left(self):
        if(self.position >=1):
            self.position-=1

    def right(self):
        if(self.position <23):
            self.position+=1

    def draw(self):
        print("."*self.position+"*"+"."*(23-self.position))

if (__name__ == "__main__"):
    isRunning = True
    star = Star()
    while(isRunning == True):
        os.system("clear")
        star.draw()
        command = input("请输入移动星星的指令（L/l or R/r）：")
        if(command.upper() == 'L'):
            star.left()
        if(command.upper() == 'R'):
            star.right()
        if(command.upper()=="EXIT"):
            isRunning = False