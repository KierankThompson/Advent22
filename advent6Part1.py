s = open("advent6.txt","r")
s = s.readlines()
ans = 0
for i in s:
    for j in range(4,len(i)+1):
        if len(set(i[j-4:j])) == 4:
            ans += j
            break
print(ans)