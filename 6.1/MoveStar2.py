from random import randint

class Star:
    def __init__(self):
        self.x = randint(0,9)
        self.y = randint(0,9)
    def left(self):
        if(self.x >=1):
            self.x-=1

    def right(self):
        if(self.x <9):
            self.x+=1
    def up(self):
        if(self.y >=1):
            self.y-=1

    def down(self):
        if(self.y <9):
            self.y+=1

    def draw(self):
        for posy in range(0,10):
            if(posy == self.y):
                print("."*self.x+"*"+"."*(9-self.x))
            else:
                print("."*10)

if (__name__ == "__main__"):
    isRunning = True
    star = Star()
    while(isRunning == True):
        star.draw()
        command = input("请输入移动星星的指令（L/l、R/r、U/u or D/d）：")
        if(command.upper() == 'L'):
            star.left()
        if(command.upper() == 'R'):
            star.right()
        if(command.upper() == 'U'):
            star.up()
        if(command.upper() == 'D'):
            star.down()
        if(command.upper()=="EXIT"):
            isRunning = False