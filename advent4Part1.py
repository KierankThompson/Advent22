s = open("advent4.txt","r")
ans =  0
for i in s:
    i3 = i.split(",")[0]
    i4 = i.split(",")1]
    p1Min = i3.split("-")[0]
    p1Max = i3.split("-")[1]
    p2Min = i4.split("-")[0]
    p2Max = i4.split("-")[1]
    if (p2Max >= p1Max and p2Min <= p1Min) or (p1Max >= p2Max and p1Min <= p2Min):
        ans += 1
print(ans)