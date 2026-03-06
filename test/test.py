def addNumbers(a, b):
    return a + b

def subtractNumbers(a, b):
    return a - b

def multiplyNumbers(a, b):
    return a * b

def divideNumbers(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def getRemainder(a, b):
    return a % b

def getFactorial(a):
    res = 1
    for i in range(1, a + 1):
        res *= i
    return res

def checkIfPrime(a):
    if a <= 1:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
    return True

def checkIfEven(a):
    return a % 2 == 0

def checkIfOdd(a):
    return a % 2 != 0

def checkIfGreaterThan(a, b):
    return a > b

def checkIfLessThan(a, b):
    return a < b

def checkIfEqualTo(a, b):
    return a == b

def checkIfBetween(a, b, c):
    return b >= a and b <= c
def validateNumber(a, b):
    return isinstance(a, (int, float)) and isinstance(b, (int, float))

def subtractNumber(a, b):
    return a - b


def multiplyNumbers(a, b):
    return a * b

if __name__ == '__main__':
    res = addNumbers(2, 6)
    val = validateNumber(2, 7)
    sub =  subtractNumber(10, 4)
    mult = multiplyNumbers(3, 4)
    div = divideNumbers(8, 2)
    rem = getRemainder(9, 4)
    fact = getFactorial(5)
    prime = checkIfPrime(7)
    even = checkIfEven(6)
    odd = checkIfOdd(5)
    gt = checkIfGreaterThan(5, 4)
    lt = checkIfLessThan(3, 5)
    eq = checkIfEqualTo(5, 5)
    btw = checkIfBetween(1, 5, 5)
    print(res)
    print(val)
    print(sub)
    print(mult)
    print(div)
    print(rem)
    print(fact)
    print(prime)
    print(even)
    print(odd)
    print(gt)
    print(lt)
    print(eq)
    print(btw)

