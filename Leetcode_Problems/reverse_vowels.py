def reverseVowels( s):
        vows = ['a','e','i','o','u','A','E','I','O','U']
        d = []
        
        for i in range(len(s)):
            if s[i] in vows:
                d.append(s[i])
        d = d[::-1]
        w = ''
        for i in range (len(s)):
            if s[i] not in vows:
                w = w+s[i]
            else:    
                w = w + d[0]
                d = d[1:]
        return(w) 

### to test
t1 = reverseVowels("hello")       
t2 = reverseVowels("leetcode")

print('Test1 Result:', t1)
print('Test2 Result:', t2)