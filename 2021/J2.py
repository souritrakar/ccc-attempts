n = int(input("Enter number of auction players"))

bids = []
for i in range(0,n):
    name = input("Enter player name")
    bid = int(input("Enter bid for "+ name))
    bids.append([name,bid])

print(bids)

greatest = ["", 0]

def findIndex(array, el):
    for i in range(0, len(array)):
        if(array[i][0] == el):
            return i
        else:
            return 0
    
for i in range(0, n):
    if(bids[i][1]>greatest[1]):
        greatest[1] = bids[i][1]
        greatest[0] = bids[i][0]
    elif bids[i][1] == greatest[1]:
        compareInd = findIndex(bids, greatest[0])
        currentInd = findIndex(bids, bids[i][0])
        
        if currentInd < compareInd:
            
            greatest[0] = bids[i][0]
            greatest[1] = bids[i][1]
        
    
print(greatest[0] + " wins with "+ str(greatest[1]))
    
