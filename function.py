from calcFunctions import factorial, decToBin, binToDec, decToRoman, romanToDec

functionMap = [
    ('factorial (!)', factorial),
    ('-> binary', decToBin),
    ('binary -> dec', binToDec),
    ('-> roman', decToRoman),
    ('roman -> dec', romanToDec),
]

functionList = [x[0] for x in functionMap] 
def findFunction(key):
    return functionMap[functionList.index(key)][1]