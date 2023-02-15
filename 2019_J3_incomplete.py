n = int(input("Enter no. of lines"))

def find_n_occurence(string, target):
    counter = 0
    for i in range(len(string)):
        if string[i] == target:
            counter+=1
    return counter

res = []

for i in range(n):
    sentence = input("Enter sentence")
    char_occurrences = {}
    
    for char in sentence:
        if char in char_occurrences:
            char_occurrences[char] += 1
        else:
            char_occurrences[char] = 1
    
    for el in char_occurrences:
        print(char_occurrences[el],el,end=" ")
