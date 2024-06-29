### Stratascratch Algorithm Questions
### Given a list of integers, find out how many additions are needed for each element 
### so that each integer appears with equal frequency "


def equal_frequency(nums):
    """
    :type nums: List[int]
    :rtype: Dict[int, int]
    """
    b = nums
    d2 = {}
    for i in range(len(b)):
        if b[i] in d2:
            d2[b[i]] =d2[b[i]] + 1
        else:
            d2[b[i]] = 1
    m = max(d2.values())
    d3 = {}
    for k in d2.keys():
        if d2[k] < m:
            d3[k] = m-d2[k]    
            
    return(d3)    

### test the function
b = [1, 3, 1, 2, 2, 4, 5]    
ans = equal_frequency(b)
print(ans)