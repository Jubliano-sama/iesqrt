number = 523912
iterations = 100
neg = ""

if number < 0:
    number = -number
    neg = "i"

currentGuess = number
iterativeAdd = currentGuess / 2

for x in range(iterations):
    if (currentGuess ** 2).__round__(9) < number:
        currentGuess += iterativeAdd
        iterativeAdd /= 2
    elif (currentGuess ** 2).__round__(9) > number.__round__():
        currentGuess -= iterativeAdd
        iterativeAdd /= 2
    else:
        print("Found precise root!:")
        print(currentGuess.__str__() + neg)
        break
    print(currentGuess.__str__() + neg)
