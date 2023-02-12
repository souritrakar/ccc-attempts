phone_dict = {
    2:['a','b', 'c'],
    3:['d','e', 'f'],
    4:['g','h', 'i'],
    5:['j','k', 'l'],
    6:['m','n', 'o'],
    7:['p','q', 'r', 's'],
    8:['t','u', 'v'],
    9:['w','x', 'y', 'z'],
    0:[' '],
    
}
letter_dict = {}
for key, value in phone_dict.items():
    for letter in value:
        letter_dict[letter] = key

res = []
while True:
    word = input()
    if word=="halt":
        break
    else:
        seconds = 0
        for i in range(len(word)):
            letter = word[i]
            letter_button = letter_dict[letter]
            letter_idx_button = phone_dict[letter_button].index(letter)+1
            seconds+=letter_idx_button
            
            if i>0 and letter_dict[word[i-1]] == letter_button :
                seconds+=2
    res.append(seconds)
    
for el in res:
    print(el)
        
