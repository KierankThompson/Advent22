s = open("advent1.txt","r")
guess = [0] * 3
curGuess = 0
for i in s:
    if i == "\n":
        if curGuess > guess[2]:
            guess[2] = curGuess
        curGuess = 0
    else:
        curGuess += int(i)
    guess.sort(reverse=True)
print(sum(guess))