## Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.
## A subarray is a contiguous part of an array.
### Example 1:
###  Input: nums = [4,5,0,-2,-3,1], k = 5
###    Output: 7

### Explanation: There are 7 subarrays with a sum divisible by k = 5: 
### [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

##---------------------------------------------------------------------------------------------##

def subarr_divisible(x,div):
    prefix_sum = []
    pre_mod =[]
    s = 0
    d = {}
    for i in range(len(x)):
        s = s+x[i]
        prefix_sum.append(s)
        pre_mod.append(abs(s)%div)
        
    for ele in pre_mod:
        if ele in d:
            d[ele] += 1
        else:
            d[ele] = 1
    
    res = 0   
    for k in d.keys():
        if d[k] > 1 and k>0:
            res = res + d[k]*(d[k]-1)//2
        elif k == 0:
            res = res + (d[k]*(d[k]-1)//2) + d[k]  
    return(res)    

## test
t1 = subarr_divisible([-1,-9,-4,0],9)
t2 = subarr_divisible([4,5,0,-2,-3,1],5)

print('Test1 Result:',t1)
print('Test2 Result:',t2)

