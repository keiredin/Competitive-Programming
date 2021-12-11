def sortColor(nums):
    length = len(nums)
    for i in range(length):
        minV_index = i
        for j in range(i+1, length):
            if(nums[j] < nums[minV_index]):
                nums[minV_index], nums[j] = nums[j], nums[minV_index]
    return nums

print(sortColor([2,0,2,1,1,0]))