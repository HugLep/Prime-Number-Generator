primeNumbers = []
Numbers = []
currentNumber = 2
currentNumber1 = 0
currentMutiple = 1
startingNumber = 2


howManyPrimes = int(input("Vous cherchez les nombres premiers inférieurs ou égal à combien ? "))
howManyPrimes = howManyPrimes - 1

while len(primeNumbers) < howManyPrimes:
    primeNumbers.append(currentNumber)
    currentNumber = currentNumber + 1

currentNumber3 = 0


while currentNumber3 < len(primeNumbers):

    while currentNumber1 < howManyPrimes:
        currentNumber = primeNumbers[currentNumber3]
        currentMutiple = currentMutiple + 1

        currentNumber1 = currentNumber * currentMutiple

        if currentNumber1 in primeNumbers :
            primeNumbers.remove(currentNumber1)
            print("Le nombre : ", currentNumber1, " a été supprimé")
    print("Les mutilpes de : ", currentNumber, " ont été supprimé")
    currentNumber3 = currentNumber3 + 1
    currentNumber = 0
    currentNumber1 = 0
    currentMutiple = 1


print(" ")
print(" ")
print("Les nombres premiers inférieur à ", howManyPrimes, " sont :")
print(primeNumbers)
print(" ")
howManyPrimes = howManyPrimes + 1
print("Il y a ", len(primeNumbers), " nombres premiers inférieur à ", howManyPrimes)
