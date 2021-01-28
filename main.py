number = 200000000000000000
iterations = 100
currentGuess = number / 2
iterativeAdd = currentGuess / 2

for x in range(iterations):
    if currentGuess ** 2 < number:
        currentGuess += iterativeAdd
        iterativeAdd /= 2
    elif currentGuess ** 2 > number:
        currentGuess -= iterativeAdd
        iterativeAdd /= 2
    print(currentGuess)
