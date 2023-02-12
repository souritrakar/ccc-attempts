K = int(input())
word = input()
res = ""

for i in range(0, len(word)):
    letter = word[i]
    shift = ((3*(i+1) + K))%26
    temp = (ord(letter) - shift) 
    
    if temp<65:
        temp +=26
    
    res+=chr(temp)
print(res)
