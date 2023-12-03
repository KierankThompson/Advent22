s = ["vJrwpWtwJgWrhcsFMMfFFhFp"]
ans = 0
for i in s:
    setL = set()
    ans2 = []
    j = 0
    for j in range(len(i) // 2):
        setL.add(i[j])
    for j in range(len(i)):
        if i[j] not in setL:
            ans2.append(i[j])
    minL = 100000
    for a in range(len(ans2)):
        if ord(ans2[a]) >= 97 and ord(ans2[a]) <= 122:
            minL = min(minL,ord(ans2[a]) - 96)
        elif ord(ans2[a]) <= 90 and ord(ans2[a]) >= 65:
            minL = min(minL,ord(ans2[a]) - 38)
    if minL != 100000:
        ans += minL
print(ans)

