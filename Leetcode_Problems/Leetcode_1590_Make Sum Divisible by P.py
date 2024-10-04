def make_divisible(nums,p):
    ## # If the total sum is already divisible by p, no subarray needs to be removed
          
    tot_sum = sum(nums)
    rem = tot_sum % p
    if rem == 0:
        return 0
    ## # Initialize min_len to the size of the array
    min_len = len(nums)
   
    # Try removing every possible subarray
                   
    for i in range(len(nums)):
        sub_sum = 0
        for j in range(i,len(nums)):
            # Calculate the subarray sum
            sub_sum += nums[j]
<<<<<<< HEAD
            print('sub array sum:',sub_sum)
            
            # Check if removing this subarray makes the remaining sum divisible by p
            rem_sum = (tot_sum-sub_sum)%p 
            print('remaining sum:', rem_sum)
=======
            ##print('sub array sum:',sub_sum)
            
            # Check if removing this subarray makes the remaining sum divisible by p
            rem_sum = (tot_sum-sub_sum)%p 
            ##print('remaining sum:', rem_sum)
>>>>>>> a6af0f9 (Make_sum_divisible_bruteforce)
            
            # Update the smallest subarray length

            if rem_sum == 0:
                min_len = min(min_len,j-i+1)
<<<<<<< HEAD
            print('minimum length:',min_len)   
            print()
=======
            ##print('minimum length:',min_len)   
            ##print()
>>>>>>> a6af0f9 (Make_sum_divisible_bruteforce)
    
    # If no valid subarray is found, return -1
    if min_len != len(nums):
        return min_len
    else:
        return -1
<<<<<<< HEAD
              
=======

print('Test Cases')
a = [3,1,4,2]
p = 6
t1 = make_divisible(a,p)
print('Test 1:',t1)         

a = [6,3,5,2]
p = 9
t2 = make_divisible(a,p)
print('Test 2:',t2)  

a = [1,2,3]
p = 3
t3 = make_divisible(a,p)
print('Test 3:',t3)  
>>>>>>> a6af0f9 (Make_sum_divisible_bruteforce)
