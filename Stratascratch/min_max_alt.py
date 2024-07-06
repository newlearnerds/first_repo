def modify_array(arr):
    """ 
    :type arr: List[int]
    :rtype: List[int]
    """
    x = []
    l = len(arr)
    arr = sorted(arr)
    for i in range(l//2):
        
        x.append(arr[i])        
        x.append(arr[l-i-1])
     
    return x
    

## to test
input1 = [13, 7, 8, 3, 2, 10, 15, -1]
output1 = modify_array(input1)

input2 = [-5, -12, -1, 7, 14, -7, 3, 6]
output2 = modify_array(input2)

input3 = [3, 6, 9, -10, -5, -2, 0, 8]    
output3 = modify_array(input3)

print('Test1:',output1)
print('Test2:',output2)
print('Test3:',output3)