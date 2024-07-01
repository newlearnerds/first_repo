def threeConsecutiveOdds(arr):
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i] = 0
        else:
            arr[i] = 1
    #print(arr)
    for i in range(len(arr)):
        #print(arr[i:i+3])
        if sum(arr[i:i+3]) == 3:
            c = 1
            break
        else:
            c = 0
    #print(c)        
    if c == 1:
        return True
    else:
        return False

### to test
t1 = threeConsecutiveOdds([2,6,4,1])
t2 = threeConsecutiveOdds([1,2,34,3,4,5,7,23,12])   

print("Test Result1:", t1)
print("Test Result2:", t2)