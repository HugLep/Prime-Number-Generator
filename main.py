primeNumbers = [2]
otherNumbers = []
startingNumber = 3
currentNumber = startingNumber
divider = 2

print("WARNING: Asking for more than 1000 numbers is not recommended, it will require a lot of resources from your computer")
howManyPrimes = int(input("How many Prime Numbers do you want to have ? "))

while len(primeNumbers) != howManyPrimes:
    result = currentNumber / divider
    resultIsInt = result

    if float(resultIsInt).is_integer():
        otherNumbers.append(currentNumber)
        currentNumber = currentNumber + 1
        divider = 2

    else:
        x = divider + 1
        if x < (currentNumber / 2):
            divider = x
        else:
            primeNumbers.append(currentNumber)
            currentNumber = currentNumber + 1
            divider = 2

print(" ")
print("Here are ", howManyPrimes, " Prime Numbers that have been generated :")
print(primeNumbers)



