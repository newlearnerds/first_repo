def string_del(s):
    x = ''
    c =0
    for i in range(len(s)):
        x = x + s[i]
        print(i,'x:',x)
        n = len(x)
        print(s[i+1:i+1+n])
        if x == s[i+1:i+n+1]:
            c += 1
            print('matched part:',x)
            print('string:',s)
            s = s.replace(x,'')
            print('truncated string:', s)
        #else:
            #x= x+s[i+1]
            #print('new x:',x)
    return c      

## test:
s = 'abcabca'
test1 = string_del(s) 
print(test1) 