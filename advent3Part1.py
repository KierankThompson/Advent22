s = open("advent3.txt","r")
ans = 0
for i in s:
    setL = set()
    ans2 = set()
    j = 0
    for j in range(len(i) // 2):
        setL.add(i[j])
    for p in range(j+1,len(i)):
        if i[p] in setL:
            ans2.add(i[p])
    for a in ans2:
        if ord(a) >= 97 and ord(a) <= 122:
             ans += ord(a) - 96
        elif ord(a) <= 90 and ord(a) >= 65:
             ans += ord(a) - 38
print(ans)

