def findUnsortedSubarray(nums):
        
    minimum, maximum = float('inf'), float('-inf')
    left_boundary, right_boundary = -1, -1
    length = len(nums)
      
    for i in range(length):

        if maximum > nums[i]:
            right_boundary = i
        else:
            maximum = nums[i]
                    
        if minimum < nums[length - i - 1]:
            left_boundary = length - i - 1
        else:
            minimum = nums[length - i - 1]
           
        
    return 0 if right_boundary == -1 else right_boundary - left_boundary + 1

arr1 = [1,3,2,2,2]
t1 = findUnsortedSubarray(arr1)
print('Test 1:', t1)

arr2 = [2,6,4,8,10,9,15]
t2 = findUnsortedSubarray(arr2)
print('Test 2:', t2)

arr3 = [2]
t3 = findUnsortedSubarray(arr3)
print('Test 3:', t3)