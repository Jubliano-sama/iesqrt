number = 4
iterations = 100
currentGuess = number
iterativeAdd = currentGuess / 2

for x in range(iterations):
    if currentGuess ** 2 < number:
        currentGuess += iterativeAdd
        iterativeAdd /= 2
    elif currentGuess ** 2 > number:
        currentGuess -= iterativeAdd
        iterativeAdd /= 2
    print(currentGuess)
