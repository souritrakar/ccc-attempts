bl = int(input("Enter temperature at which water boils"))

if bl >= 80 and bl<=200:
    p = (5*bl)-400
    position = 0;
    if bl==100:
        position = 0;
    elif bl>100:
        position = -1
    else:
        position=1
    
    print("Pressure is"+ str(p) + "\n"+str(position))
        
    
else:
    print("Invalid boiling point input")


