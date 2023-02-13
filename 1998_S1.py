n = int(input())
res = []
for i in range(n):
    sentence = input().split(" ")
    to_append = ""
    for j in range(len(sentence)):
        if len(sentence[j]) == 4:
            to_append += "**** "
        else:
            to_append += sentence[j]+" "
    res.append(to_append)

for word in res:
    print(word.strip())
            
