# Program Name: Numbering Systems Converter
# Program Description: A numbering system converter that converts from the 4 basic systems: Binary, Decimal, Octal, Hexadecimal and to them depending on the user's preference.
# Last Modification Date: 3/8/2024
# Author: Adham Ghallab
# Credit: Another individual from my college helped in the making of some functions

# If conditions to return the base of the inputted value
def base_num(letter):
    if letter == 'A':
        return 10
    elif letter == 'B':
        return 2
    elif letter == 'C':
        return 8
    else:
        return 16

# Tests if the input corresponds with the user choices (valid) 
def validity(num, base):
    num = num.upper()
    range = "0123456789ABCDEF" 
    for digit in num:
        if digit not in range[:base]:
            return False
    return True
        
# Main Function which chooses the appropriate conversion function 
def assembly(num, from_base, to_base):
    if to_base == 'A':
        return to_decimal(num, from_base)
    else:
        return to_base_n(num, from_base)

#Converts the number from whichever base the user inputs to a decimal 
def to_decimal(num, from_base):
    result = 0
    len_num = len(num) - 1 
    hex_char = "0123456789ABCDEF"
    num = num.upper()
    for index in num:
        if from_base == 'D':
            result += hex_char.index(index) * (base_num(from_base) ** len_num)
            
        else:
            result += int(index) * (base_num(from_base) ** len_num)
        len_num -= 1
    return result

#Converts the number from decimal to whichever base the user inputs (inverse of to_decimal function)
#Deals with the problem in a clever way minimizing the number of functions needed
def to_base_n(num, from_base):
    num = int(to_decimal(num, from_base))
    base = base_num(to_base)
    final = "" #Dealing with the binary number as a string for concatenation
    
    #if user wants to convert to a certain base other than hexadecimal it's the same procedure 
    if to_base != 'D':
        remainder = 0
        while num > 0:
            remainder = num % base 
            num //= base
            final = str(remainder) + final
        return final
    
    #Hexadecimal Conversion function
    hexa_bet = "0123456789ABCDEF"    #Hexadecimal Range or alphabet (hexa_bet)
    while num > 0:
        remainder = num % base
        num //= base
        final = str(hexa_bet[remainder]) + final
    return final


# Main Menu Function
while True:
    print("**Numbering System Converter**\nA) Insert a new number\nB) Exit Program\n")
    startprogram = input().upper()
    
    if startprogram == 'A':
        #Start of the Program
        num = input("Please insert a number\n\n").upper()

        # Checks if the number entered is valid (highest valid base is 16)
        valid_chars = set("0123456789ABCDEF")
        if not all(char in valid_chars for char in num):
            print("Invalid number, Please try again and enter a valid number\n")
            continue

        while True: #Menu #2
            from_base = input("** Please select the base you want to convert a number from**\nA) Decimal\nB) Binary\nC) Octal\nD) Hexadecimal\n").upper()
            if from_base!= 'A' and from_base!= 'B' and from_base!= 'C' and from_base!='D':
                print("Please select a valid option")
                continue
            if validity(num, base_num(from_base)) == False:
                print("Please Select A Proper Base For The Entered Number\n")
                continue
            break
        while True: #Menu #3
            to_base = input("** Please select the base you want to convert a number to**\nA) Decimal\nB) Binary\nC) Octal\nD) Hexadecimal\n").upper()
            if to_base!= 'A' and to_base!= 'B' and to_base!= 'C' and to_base!='D': 
                print("Please select a valid option")
                continue
            break
        
        answer = assembly(num, from_base, to_base) 
        print("\nYour Answer is :", answer, "\n")
        
    elif startprogram == 'B':
        break
        
    else:
        print("Please enter a valid input\n")
        
print("Exiting Program")
