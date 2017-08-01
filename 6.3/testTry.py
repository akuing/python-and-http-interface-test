def testTry1():
    try:
        return 0
    except(Exception):
        return 1
    finally:
        return 2

def testTry2():
    try:
        raise Exception
        return 0
    except(Exception):
        return 1
    finally:
        return 2

def testTry3():
    try:
        "2"+2
        return 0
    except(Exception):
        return 1
    finally:
        return 2
def testTry11():
    try:
        return 0
    except(Exception):
        return 1

def testTry21():
    try:
        raise Exception
        return 0
    except(Exception):
        return 1

def testTry31():
    try:
        "2"+2
        return 0
    except(Exception):
        return 1

def testTry32():
    try:
        "2"+2
        return 0
    except(Exception):
        return 1
    finally:
        return 2

    return 3

if(__name__ == "__main__"):
    print(testTry1())
    print(testTry2())
    print(testTry3())
    print(testTry11())
    print(testTry21())
    print(testTry31())
    print(testTry32())
