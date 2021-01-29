def findRoot(number):
    neg = ""
    if number < 0:
        number = -number
        neg = "i"
    currentGuess = number
    iterativeAdd = currentGuess / 2
    while (currentGuess ** 2).__round__(9) != number:
        if (currentGuess ** 2).__round__(9) < number:
            currentGuess += iterativeAdd
            iterativeAdd /= 2
        elif (currentGuess ** 2).__round__(9) > number.__round__():
            currentGuess -= iterativeAdd
            iterativeAdd /= 2
    print("Found precise root!:")
    print(currentGuess.__str__() + neg)


number = input("Enter a number to find the square root: ")
while not number.isnumeric():
    number = input("Please enter a valid number: ")

findRoot(int(number))
