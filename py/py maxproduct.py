def maxProduct(nums):
    cntX = 0
    for i in nums:
        for j in nums:
            if(i == j):
                continue
            if(cntX < i*j):
                cntX = i*j
    return cntX


print(maxProduct([5, 20, 2, 6]))
print(maxProduct([10, -20, 0, 3]))
