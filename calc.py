def valid_number(number):
    while True:
        operand = input("Number " + str(number) + ": ")
        try:
            return float(operand)
        except:
            print("Invalid operand,try again.")
 
operand1 = valid_number(1)
operand2 = valid_number(2)


# while True:
#     operand1 = input("Enter first number: ")
#     try:
#         operand1 = float(operand1)
#         break
#     except:
#         print("Invalid operand,try again.")

# while True:
#     operand2 = input("Enter first number: ")
#     try:
#         operand2 = float(operand2)
#         break
#     except:
#         print("Invalid operand,try again.")        
        

sign = input("Enter your desired sign: ")

#print(operand1, sign, operand2) 
# valid = False   
# try:
#     operand1 = float(operand1)
#     operand2 = float(operand2)
#     valid = True
# except:
#     print("Invalid operands")    

# if valid:    
result = 0   
if sign == "+":
    result = float(operand1) + float(operand2)
elif sign == "-":
    result = float(operand1) - float(operand2)
elif sign == "/":
    if float(operand2) != 0:
        result = float(operand1) / float(operand2) 
    else:
        print("Division by ZERO")    
elif sign == "*":
    result = float(operand1) * float(operand2)
else:
    print("Invalid sign.")    

print(result)    
         
