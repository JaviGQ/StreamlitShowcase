import math
from datetime import datetime as DateTime, timedelta as TimeDelta

"""print("Divisible by 7")
for i in range(2000, 3202):
    if i % 7 == 0 and i % 5 == 0:
        print(i)

print("\nFactorial")
num = input("Enter a number to find its factorial: ")
print(math.factorial(int(num)))

print("\nDictionary")
dict = input("Enter a number for the size of the dictionary: ")
fullDict = {}
for i in range(1, int(dict) + 1):
    fullDict[i] = [i * i]

print(fullDict)


userInfo = input("Please enter your name and age: ")
name, age = userInfo.split()
age = int(age)
till100 = 100 -  age
print(f"{name} will turn 100 in the year {till100 + 2025}")



numList = input("Please enter a numbers to find its divisors: ")
numList = int(numList)
for i in range(1, numList + 1):
    if numList % i == 0:
        print(i)


a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
newList = [x for x in a if x % 2 == 0]
print(newList)



listA = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 81]
listB = [2, 4, 19, 316, 25, 36, 349, 624, 831, 1000, 100, 81]
newList = []
for x in listA:
    if listB.count(x) > 0 and newList.count(x) == 0:
        newList.append(x)
print(newList)


numList = {
    "a": [1, 4, 9, 16, 25, 36, 49, 64, 81, 100],
    "b": [2, 4, 19, 316, 25, 36, 349, 624, 831, 100],
}
sum = 0
for x in numList:
    for y in numList[x]:
        sum += y

print(sum)

now = DateTime.today()
birth = now + TimeDelta(seconds=109)
print(birth)



prime = input("Please enter a number to see if it is prime: ")
prime = int(prime)

isPrime = False
for i in range(1, int(prime) + 1):
    if prime % i == 0 and i != 1 and i != prime:
        isPrime = False
        break
    else: isPrime = True

if isPrime:
    print(prime, " is a prime number")
else:
    print(prime, " is not a prime number")



input = input("Please enter a word: ")
if len(input) >= 3:
    if input[-3:] == "ing":
        input = input + "ly"
    else:
        input = input + "ing"
    print(input)
else:
    print(input)


ascii = input("Enter a character to get its ASCII value: ")
print(f"Character: {ascii}, ASCII: ", ord(ascii))


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n+1):
            a, b = b, a + b
        return b

fib = input("Please enter a number to find the Fibonacci series: ")
fib = int(fib)
print(fibonacci(fib))

"""

nums = input("Please enter a list of numbers: ")
a, b, c = nums.split()
a, b, c = int(a), int(b), int(c)
if a > b:
    if a > c:
        print(a, " is the largest number")
    else:
        print(c, "is the largest number")
else:
    if b > c:
        print(b, "is the largest number")
    else:
        print(c, "is the largest number")
