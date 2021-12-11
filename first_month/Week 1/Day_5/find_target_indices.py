def targetIndices(nums,target):
    length = len(nums)
    for i in range(length):
        minV_index = i
        for j in range(i+1, length):
            if(nums[j] < nums[minV_index]):
                nums[minV_index], nums[j] = nums[j], nums[minV_index]

    indices = []
    for i in range(length):
        if(nums[i] == target):
            indices.append(i)
    return indices

print(targetIndices([1,2,5,2,3],5))

