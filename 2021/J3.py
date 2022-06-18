instructions = []
i = 0
direction = ""
    
while(True):
    
    ins = input()
    
    if(len(ins) ==5):
        
        if(ins == "99999"):
            break
        elif i==0 and ins[:2]=="00" or i==0 and ins=="99999":

            break
        
        else:
            instructions.append(ins)
        i+=1
        

for i in range(0, len(instructions)):
    
    p1 = instructions[i][:2]
    p2 = instructions[i][-3:]
    p10 = int(p1[0])
    p20 = int(p1[1])
    
    sumN = p10+p20
  
  
    if( sumN % 2 != 0 ):
        direction = "left"
        print(direction + " "+ p2)
    elif ( sumN % 2 == 0 and sumN!= 0 ):
        direction = "right"
        print(direction + " "+ p2)
    elif sumN==0:
        print(direction + " "+ p2)
