s = open("advent1.txt","r")
guess = 0
curGuess = 0
for i in s:
    if i == "\n":
        guess = max(curGuess,guess)
        curGuess = 0
    else:
        curGuess += int(i)
print(guess)