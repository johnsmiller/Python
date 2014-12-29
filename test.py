__author__ = 'John'
def testFunc(total, tipperc):
    inputpeople = input("Number of people:")
    try:
        return round((total*(1+tipperc/100))/int(inputpeople),2)
    except:
        print("Error: Non-number or invalid number encountered")
        return 0

print(testFunc(100, 9.325))