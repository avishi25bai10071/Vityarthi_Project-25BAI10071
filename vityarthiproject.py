num1 = int(input("Enter the number you want to be printed: "))
l = []
orig = []      # To store original number for each digit

for i in range(1, num1+1):
    num1_str = str(i)
    le = len(num1_str)

    for j in range(le):
        digit = int(num1_str[j])
        l.append(digit)
        orig.append(i)     # store original number 

#removing last digit
del l[-1]
del orig[-1]

print("Digit list:", l)

index = int(input("Enter index for whose original number you want to be printed : "))
index -= 1     

if 0 <= index < len(orig):
    print("Number:", orig[index])
else:
    print("Invalid")