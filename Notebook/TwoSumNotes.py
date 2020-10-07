nums3 = [2,7,11,15]
ht = {}
target = 26
for i, n in enumerate(nums3):
    if target - n in ht:
        print([ht[target - n], i])
        break
    ht[n] = i
    print(ht)
    print(ht[n])
print([])