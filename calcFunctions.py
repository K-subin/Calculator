from math import factorial as fact

def factorial(numStr):
    try:
        n = int((numStr))
        r = str(fact(n))
    except ValueError:
        r = '수식이 올바르지 않습니다'
    except OverflowError:
        r = '인수는 2147483647을 초과할 수 없습니다'
    return r

def decToBin(numStr):
    try:
        n = int(numStr)
        r = bin(n)[2:]
    except ValueError:
        r = '수식이 올바르지 않습니다'
    return r

def binToDec(numStr):
    try:
        n = int(numStr, 2)
        r = str(n)
    except ValueError:
        r = '수식이 올바르지 않습니다'
    return r

romans = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
         (100, 'C'),  (90, 'XC'),  (50, 'L'),  (40, 'XL'),
          (10, 'X'),   (9, 'IX'),   (5, 'V'),   (4, 'IV'),
           (1, 'I')
    ]

def decToRoman(numStr):
    try:
        n = int(numStr)
    except ValueError:
        return '수식이 올바르지 않습니다'
    
    if n >= 4000:
        return '인수는 4000을 초과할 수 없습니다'
    if n < 0:
        return '음수는 로마숫자로 표현할 수 없습니다'

    result=''
    for value, letters in romans:
        while n >= value:
            result += letters
            n -= value
    
    return result

def romanToDec(numStr):
    result = 0
    for value, letters in romans:
        while(numStr.find(letters) == 0):
            result += value
            numStr = numStr[len(letters):]
        if not numStr:
            break
        
    if numStr:
        return '올바른 로마숫자 표현이 아닙니다'

    return str(result)