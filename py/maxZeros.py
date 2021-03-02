def maxZeros(nums):
    maxN = 0
    cnt = 0
    for i in nums:
        if(i == 0):
            cnt += 1
            if(maxN < cnt):
                maxN = cnt
        else:
            cnt = 0
    return maxN

result1 = maxZeros([0, 1, 0, 0])
result2 = maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0])
result3 = maxZeros([1, 1, 1, 1, 1])

print(result1)
print(result2)
print(result3)
