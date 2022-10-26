n = int(input("Enter N"))
yesterday = "CC..C"
today =     ".CC.."
common = 0

for i in range(0, n):
    if(yesterday[i] == "C" and today[i] == "C"):
        common+=1

print(common)

#The first line of input contains the integer N (1 ≤ N ≤ 100). The second and third lines of input contain N characters each. The second line of input records the information about yesterday’s parking spaces, and the third line of input records the information about today’s parking spaces. Each of these 2N characters will either be C to indicate an occupied space or . to indicate it was an empty parking space
