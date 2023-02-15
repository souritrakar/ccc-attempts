n = int(input("Enter no. of lines"))

def find_n_occurence(string, target):
    counter = 0
    for i in range(len(string)):
        if string[i] == target:
            counter+=1
    return counter
    
index_dict = {}

for i in range(n):
    sentence = input("Enter sentence")
    char_occurrences = {}
    
    for char in sentence:
        if char in char_occurrences:
            char_occurrences[char] += 1
        else:
            char_occurrences[char] = 1
    res = []
    for j, (key, value) in enumerate(char_occurrences.items()):
        
        res.append((value,key))
    index_dict[i] = res
    
for el in index_dict:
    for individual in index_dict[el]:
        print(*individual, sep = " " )

            
