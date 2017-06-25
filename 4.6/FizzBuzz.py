maxnum = input("请输入一个小于100的数字:")
maxnum = int(maxnum)
if(maxnum<1 or maxnum >100):
    print("请输入1到100之间的数字。")
    exit()
for i in range(1,maxnum+1):
    if(i % 3 ==0 and i % 5 ==0):
        print("FizzBuzz")
    elif(i % 3 == 0):
        print("Fizz")
    elif (i % 5 == 0):
        print("Buzz")
    else:
        print(i)



