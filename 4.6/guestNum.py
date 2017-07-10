from random import randint
number = randint(1,100)
flag = True
guess = int(input('请输入一个整数: '))
while(flag):
    if guess == number:
        print('恭喜你，猜对啦！')
        break
    elif guess < number:
        print('目标数字比你输入的数字大！')
        # 你可以在此做任何你希望在该代码块内进行的事情
        guess = int(input('请重新输入一个整数: '))
    else:
        print('目标数字比你输入的数字小！')
        # 你必须通过猜测一个大于（>）设置数的数字来到达这里。
        guess = int(input('请重新输入一个整数: '))


print('Done')
