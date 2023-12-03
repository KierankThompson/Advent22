s = open("advent4.txt","r")
ans =  0
for i in s:
    i3 = i.split(",")[0]
    i4 = i.split(",")[1]
    p1Min = i3.split("-")[0]
    p1Max = i3.split("-")[1]
    p2Min = i4.split("-")[0]
    p2Max = i4.split("-")[1]
    if (int(p1Max) >= int(p2Min) and int(p1Max) <= int(p2Max)) or (int(p2Max) >= int(p1Min) and int(p2Max) <= int(p1Max)):
        ans += 1
        
print(ans)