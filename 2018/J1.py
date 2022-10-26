digits = []

for i in range(0,4):
    num = int(input("Enter digit"))
    digits.append(num)
print(digits)
if((digits[0] == 8 or digits[0] == 9) and (digits [3] == 8 or digits[3] == 9) and (digits[1] == digits[2])):
    print("ignore")
else:
    print("answer")
    
#• the first of these four digits is an 8 or 9;
#• the last digit is an 8 or 9;
#• the second and third digits are the same.
#For example, if the last four digits of the telephone number are 8229, 8338, or 9008, these are telemarketer numbers.
#Write a program to decide if a telephone number is a telemarketer number or not, based on the last four digits. If the number is not a telemarketer number, we should answer the phone, and otherwise, we should ignore it.
