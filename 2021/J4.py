line= input("Enter line")
n_string = []

swap = 0
for k in range(0, len(line)):
    n_string.append(line[k])
    
for i in range(len(n_string)):
        minI = i

        for j in range(i + 1, len(n_string)):
         
            if n_string[j] < n_string[minI]:
                minI = j
                swap+=1
         
        n_string[i], n_string[minI] = n_string[minI], n_string[i]
        


print(n_string, swap)
        
            
