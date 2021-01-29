def findRoot(number):
    neg = ""
    iterations = 0
    requiredDecimals = 10
    if number < 0:
        number = -number
        neg = "i"
    currentGuess = number
    iterativeAdd = currentGuess / 2
    while (currentGuess ** 2).__round__(requiredDecimals) != number:
        iterations += 1
        if (currentGuess ** 2).__round__(requiredDecimals) < number:
            currentGuess += iterativeAdd
            iterativeAdd /= 2
        elif (currentGuess ** 2).__round__(requiredDecimals) > number.__round__():
            currentGuess -= iterativeAdd
            iterativeAdd /= 2
        if iterations > 10000:
            print("Found mildly precise root: %s" % currentGuess)
            return

    print("Found precise root in %s iteration(s):" % iterations)
    print(currentGuess.__round__(requiredDecimals).__str__() + neg)


number = input("Enter a number to find the square root: ")
while True:
    try:
        findRoot(int(number))
        break
    except(ValueError):
        number = input("Please enter a valid number: ")


