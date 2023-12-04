s = open("advent6.txt","r")
s = s.readlines()
ans = 0
for i in s:
    for j in range(14,len(i)+1):
        if len(set(i[j-14:j])) == 14:
            print(i[j-14:j])
            ans += j
            break
print(ans)