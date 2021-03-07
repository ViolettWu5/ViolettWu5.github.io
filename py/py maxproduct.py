 maxProduct(nums):
    cntx = 0
    if len(nums) == 2:
        cntx = nums[0] * nums[1]
    else:
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                sum = nums[i] * nums[j]
                if sum > cntx:
                    cntx = sum
    return cntx


print(maxProduct([5, 20, 2, 6]))
print(maxProduct([10, -20, 0, 3]))
print(maxProduct([1,-10]))

