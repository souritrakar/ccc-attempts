adjectives = int(input())
nouns = int(input())
adj = []
nouns_arr = []

for i in range(adjectives):
    adj.append(input())

for i in range(nouns):
    nouns_arr.append(input())

for adjective in adj:
    for noun in nouns_arr:
        print(adjective+ " as "+noun)

