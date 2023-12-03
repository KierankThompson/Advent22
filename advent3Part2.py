s = open("advent3.txt","r")
ans = 0
ans2 = [0] * 53
counter = 1
for i in s:
    for j in i:
        if ord(j) >= 97 and ord(j) <= 122:
                if ans2[ord(j) - 96] == counter - 1:
                    ans2[ord(j) - 96] += 1
        elif ord(j) <= 90 and ord(j) >= 65:
                if ans2[ord(j) - 38] == counter - 1:
                    ans2[ord(j) - 38] += 1
    if counter == 3:
        counter2 = 0
        for a in range(1,len(ans2)):
            if ans2[a] == 3:
                ans += a
                counter2 += 2
        ans2 = [0] * 53
        counter = 0
    counter += 1
print(ans)

