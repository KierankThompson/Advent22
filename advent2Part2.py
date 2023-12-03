s = open("advent2.txt","r")
#XYZ = RPS, PRS, PSR, RSP, SRP, SPR
#Lose = 0, Draw = 3, Win = 6
#Rock = 1 Paper = 2 Scissor = 3
dic = {"A X":3,"A Y":4,"A Z":8,"B X":1,"B Y":5,"B Z":9,"C X":2,"C Y":6,"C Z":7}
ans = 0
for i in s:
    ans += dic[i[:3]]
print(ans)