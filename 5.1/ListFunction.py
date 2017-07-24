def foo1():
    print("this is foo1!")

def foo2():
    print("this is foo2!")

listFun = [foo1,foo2]

for function in listFun:
    function()


def foo():
    print("foo")


function = foo
function()