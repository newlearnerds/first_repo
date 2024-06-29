###  Write a short recursive Python function that finds the maximum
###  values in a sequence without using any loops.

def max_recur(s):
    n = len(s)
    if n == 1:
        return s[n-1]
    
    i = n-1
    if s[i] > s[i-1]:
        s = s[0:i-1]+s[i:]
        print('1st check true:',s)
        return max_recur(s)
    else:
        s = s[0:i]
        print('2nd check true:',s)
        return max_recur(s)
# To test the maximum recursion function    
a = max_recur([2,5,1,6,3])
print(a)   

b = max_recur([-1,0,-3,-4])
print(b)