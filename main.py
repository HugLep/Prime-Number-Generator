primeNumbers = [2]
otherNumbers = []
startingNumber = 3
currentNumber = startingNumber
divider = primeNumbers[0]
x = -1

print("WARNING: Asking for more than 5000 numbers is not recommended, it will require a lot of resources from your computer")
howManyPrimes = int(input("How many Prime Numbers do you want to have ? "))

while len(primeNumbers) != howManyPrimes:
    result = currentNumber / divider
    resultIsInt = result

    if float(resultIsInt).is_integer():
        otherNumbers.append(currentNumber)
        currentNumber = currentNumber + 1
        divider = primeNumbers[0]
        x = -1

    else:
        x = x + 1
        if x < (len(primeNumbers) - 1):

          divider = primeNumbers[x]
        else:
            primeNumbers.append(currentNumber)
            currentNumber = currentNumber + 1
            divider = primeNumbers[0]
            x = -1


print(" ")
print("Here are ", howManyPrimes, " Prime Numbers that have been generated :")
print(primeNumbers)


