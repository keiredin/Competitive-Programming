def smallerNumbersThanCurrent(nums):
    l = len(nums)
    list = []
    for i in range(l):
        count = 0
        for j in range(l):
            if(nums[j] < nums[i]):
                count += 1
                    
        list.append(count)
    return list

print(smallerNumbersThanCurrent([8,1,2,2,3]))
print(smallerNumbersThanCurrent([6,5,4,8]))
print(smallerNumbersThanCurrent([7,7,7,7,7]))