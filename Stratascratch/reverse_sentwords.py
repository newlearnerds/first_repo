def reverse_word(w):
    l = len(w)
    ans = ''
    while l > 0:
        ans = ans+w[-1]
        l= l-1
        w = w[0:l]  
        
    return ans

def reverse_letters(input_string):
    """ 
    :type input_string: str
    :rtype: str """
    input_string = input_string.split(' ')
    rev_sent = ''
    for word in input_string:
        rev_word = reverse_word(word)
        rev_sent = rev_sent +' '+ rev_word
    return rev_sent.strip()


## to test   
input1 ="The quick brown fox jumps over the lazy dog"    
output1 = reverse_letters(input1)

input2 = "Programming is fun and challenging!"
output2 = reverse_letters(input2)

input3 = "123 abc! XYZ $%^&*"
output3 = reverse_letters(input3)

print('Test1:', output1)
print('Test2:', output2)
print('Test3:', output3)
    