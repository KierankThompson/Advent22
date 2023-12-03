s = open("advent2.txt","r")
#XYZ = RPS, PRS, PSR, RSP, SRP, SPR
#Lose = 0, Draw = 3, Win = 6
#Rock = 1 Paper = 2 Scissor = 3
dic = {"A X":[4,8,8,4,3,3],"A Y":[8,4,3,3,4,8],"A Z":[3,3,4,8,8,4],"B X":[1,5,5,1,9,9],"B Y":[5,1,9,9,1,5],"B Z":[9,9,1,5,5,1],"C X":[7,2,2,7,6,6],"C Y":[2,7,6,6,7,2],"C Z":[6,6,7,2,2,7]}
ans = [0] * 6
for i in s:
    a = dic[i[:3]]
    for j in range(len(a)):
        ans[j] += a[j]
print(ans)