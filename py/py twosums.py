def twoSum(nums, target):
    for i in range(0, len(nums)):
        for j in range(0, len(nums)):
            if(i == j):
                continue
            if(target == (nums[i] + nums[j])):
                return [i, j]

result = twoSum([2, 11, 7, 15], 9)

print(result)
