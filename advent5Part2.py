s = open("advent5.txt","r")
s = s.readlines()
arr = [[] for _ in range(10)]
startAdding = False
for i in s:
    if i == "\n":
        startAdding = True
        continue
    if startAdding == False:
        for j in range(len(i)):
            if startAdding == False and i[j].isalpha():
                arr[int((j+3)/4)].append(i[j])
    else:
        nums = i.split()
        amount = int(nums[1])
        origin = int(nums[3])
        destin = int(nums[5])
        newArr = []
        while amount > 0:
            element = arr[origin].pop(0)
            newArr.append(element)
            amount -= 1
        arr[destin] = newArr + arr[destin]
ans = ""
for a in arr:
    for a2 in a:
        ans += a2
        break
print(ans)