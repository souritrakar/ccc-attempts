
instructions = []
i = 1

def printInstructions(instruction):
    p1 = instruction[:2]
    p2 = instruction[-3:]
    sumN = ((ord(p1[0]) - 0) + (ord(p1[1]) - 0))
  
    direction = ""
    
    if( sumN % 2 != 0 ):
        direction = "left"
        print(direction + " "+ p2)
    elif ( sumN % 2 == 0 and sumN!= 0 ):
        direction = "right"
        print(direction + " "+ p2)
    elif sumN==0:
        print(direction + " "+ p2)
    
    
while(True):
    
    ins = input()
    
    if(len(ins) ==5):
        
        if(ins == "99999"):
            break
        elif i==1 and ins[:2]=="00" or i==1 and ins=="99999":
            print("First number cannot start with 00")
            break
        else:
            instructions.append(ins)
        i+=1
        
    else:
        print("Has to be atleast 5")
        break
    
    
    
if not len(instructions) >=2:
    print("Not enough valid instructions")
    
else:
    for i in range(0, len(instructions)):
        printInstructions(instructions[i])
    
