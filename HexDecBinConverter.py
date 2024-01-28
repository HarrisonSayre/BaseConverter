#Conversion between decimals, binary, and hexadecimal. Yes, python has some of these built in, this is my own implentation for practice.

#Dictionaries used for conversions involving hexadecimal.
hexdigitdictionay = {"0":0, "1":1, "2":2,"3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "A":10, "B":11,"C":12, "D":13, "E":14, "F":15}
hexdigitbinarydictonary = {"0": "0000", "1": "0001", "2": "0010", "3":"0011", "4":"0100", "5":"0101", "6":"0110", "7":"0111", "8":"1000", "9":"1001",
                           "A":"1010", "B":"1011", "C":"1100", "D":"1101", "E":"1110", "F":"1111"}
binaryhexdigitdictionay = {"0000":'0', "0001":'1', "0010":'2',"0011":'3', "0100":'4', "0101":'5', "0110":'6', "0111":'7', "1000":'8', "1001":'9', 
                           "1010":'A', "1011":'B',"1100":'C', "1101":'D', "1110":'E', "1111":'F'}


#Uses a dictionary to find the decimal value of a 1-F in hexadecimal.
def HexConvert(hexdigit):
    hexletter = hexdigitdictionay.get(hexdigit)
    if hexletter != None:
        return hexletter
    return None     # This handles if there isn't a valid hexadecimal number (None will trigger checks in the converter to prompt for a correctly format number)

#Hexadecimal to Decimal
def HextoDecFor (n):
    power = len(n)-1
    total = 0
    for digit in n:
        current_digit = (HexConvert(digit.upper()))
        if current_digit == None:
            return None
        total += 16**power * current_digit
        power -= 1
    return (total)

#Decimal to Hexadecimal
def DectoHex(n):
    divised = n
    hexnumber = ""
    while divised != 0:
        remainder = divised%16
        if remainder >= 10:
            hexnumber += (chr(remainder+55))
        else:
            hexnumber += (chr(remainder+48))
        divised = divised//16
    #print(hexnumber)
    return(Reverse(hexnumber))

#Decimal to Binary using recursion
def RecursiveDectoBin(n):
    if n == 0:
        return ''
    return RecursiveDectoBin(n//2)+str(n%2)    

#Binary to Decimal conversion
def BinarytoDecimal(n):
    power = len(n)-1 # = 0
    total = 0
    for digit in n:
        if digit != '1' and digit != '0': #Not a proper binary string
            return None
        if digit == '1':
            total += 1*(2**power)
        power -= 1
    return(total)

def BinarytoHexadecimal(n):
    singlehexnum = ''
    finalhexnum = ''
    while len(n)%4 != 0:
        n = '0'+n
    for digit in n:
        if digit != '1' and digit != '0': #Not a proper binary string
            return None
        singlehexnum += digit
        if len(singlehexnum) == 4: #Hex is every four bits
            finalhexnum += binaryhexdigitdictionay.get(singlehexnum)
            singlehexnum = ''
    return finalhexnum

#Mostly just exists to show that you *could* do it
def LazyHextoBinary(n):
    return RecursiveDectoBin(HextoDecFor(n))

#Hexadecmal to Binary
def HexadecimaltoBinary(n):
    binarynum = ""
    for digit in n:
        current_digit = hexdigitbinarydictonary.get(digit)
        if current_digit == None: #Not a proper hexadecimal character
            return None
        binarynum += current_digit
        #print(binarynum)
    return binarynum        

#This is a crafted reverse, rather than a simple x[::-1] slice
def Reverse(n):
    reversed = ""
    length = len(n)-1
    for digit in n:
        reversed += (n[length])
        length -= 1
    return(reversed)

#Tester to handle individual fuctions without having to use the menu interface
def Tester(enternumber):
    #DectoHexTester
    #print(DectoHex((int(enternumber))))
    #print(HextoDecFor(DectoHex((int(enternumber)))))

    #DectoBinaryTester
    #print(RecursiveDectoBin(int(enternumber)))
    #print(BinarytoDecimal((RecursiveDectoBin(int(enternumber)))))

    #HextoDecTester
    #print(HextoDecFor(enternumber))
    #print(DectoHex(HextoDecFor(enternumber)))

    #HextoBinaryTester
    #print(HexadecimaltoBinary(enternumber))
    #print(BinarytoHexadecimal(HexadecimaltoBinary(enternumber)))

    #BinarytoDecTester
    #print(BinarytoDecimal(enternumber))
    #print(RecursiveDectoBin(BinarytoDecimal(enternumber)))

    #BinarytoHexTester
    #print(BinarytoHexadecimal(enternumber))
    #print(HexadecimaltoBinary(BinarytoHexadecimal(enternumber)))
    return

#Mostly exists so I wouldn't have to keep typing goodbye
def ExitFunction():
    print("Goodbye")
    quit()

#Seperate function for readability. Handles binary
def Binary_Sub_Menu():
    while(True):
        print("Do you want to convert to decimal or hexadecimal?. Type 'Back' to choose a different base to convert instead")
        option = input().upper().strip()
        if(option=="DECIMAL"):
            while True:
                print("Please enter the binary number you want to convert or type 'Back' to choose a different option:")
                enternumber = input().upper().strip()
                if enternumber == "EXIT":
                    ExitFunction()
                elif enternumber == "BACK":
                    break
                else:
                    answer = (BinarytoDecimal(enternumber))
                    if answer == None: #Any character other than 0 or 1 for enternumber returns None. Prompt for reentry
                        print("That is not a properly formatted binary number") 
                        continue
                    else:
                        print(answer,"\nYour number has been converted. Please enter a new base for another number you want to convert, or type exit to leave")
                        return
        elif(option=="HEXADECIMAL"):
            while True:
                print("Please enter the binary number you want to convert or type 'Back' to choose a different option:")
                enternumber = input().upper().strip()
                if enternumber == "EXIT":
                    ExitFunction()
                elif enternumber == "BACK":
                    break
                else:
                    answer = (BinarytoHexadecimal(enternumber))
                    if answer == None: #Any character other than 0 or 1 for enternumber returns None. Prompt for reentry.
                        print("That is not a properly formatted binary number")
                        continue
                    else:
                        print(answer,"\nYour number has been converted. Please enter a new base for another number you want to convert, or type exit to leave")
                        return
        elif(option=="BACK"):
            print("Choose to convert a decimal number, a binary number, or a hexadecimal number")
            return
        elif(option=="EXIT"):
            ExitFunction()
        else:
            print("Sorry, that's not one of the options.")

#Basically a copy of the above for hexadecimal
def Hexadecimal_Sub_Menu():
    while(True):
        print("Do you want to convert to decimal or binary?. Type 'Back' to choose a different base to convert instead")
        option = input().upper().strip()
        if(option=="DECIMAL"):
            while True:
                print("Please enter the hexadecimal number you want to convert or type 'Back' to choose a different option:")
                enternumber = input().upper().strip()
                if enternumber == "EXIT":
                    ExitFunction()
                elif enternumber == "BACK":
                    break
                else:
                    answer = (HextoDecFor(enternumber))
                    if answer == None:
                        print("That is not a properly formatted hexadecimal number")
                        continue
                    else:
                        print(answer,"\nYour number has been converted. Please enter a new base for another number you want to convert, or type exit to leave")
                        return
        elif(option=="BINARY"):
            while True:
                print("Please enter the hexadecimal number you want to convert or type 'Back' to choose a different option:")
                enternumber = input().upper().strip()
                if enternumber == "EXIT":
                    ExitFunction()
                elif enternumber == "BACK":
                    break
                else:
                    answer = (HexadecimaltoBinary(enternumber))
                    if answer == None:
                        print("That is not a properly formatted hexadecimal number")
                        continue
                    else:
                        print(answer,"\nYour number has been converted. Please enter a new base for another number you want to convert, or type exit to leave")
                        return
        elif(option=="BACK"):
            print("Choose to convert a decimal number, a binary number, or a hexadecimal number")
            return
        elif(option=="EXIT"):
            ExitFunction()
        else:
            print("Sorry, that's not one of the options.")

#And the above for decimal
def Decimal_Sub_Menu():
    while(True):
        print("Do you want to convert to hexadecimal or binary?. Type 'Back' to choose a different base to convert instead")
        option = input().upper().strip()
        if(option=="HEXADECIMAL"):
            print("Please enter the base 10 number you want to convert or type 'Back' to choose a different option:")
            while True:
                enternumber = input().upper().strip()
                if enternumber == "EXIT":
                    ExitFunction()
                elif enternumber == "BACK":
                    break
                try:
                    enternumber = int(enternumber) #Decimals are easy. Just check to see if it's an integer.
                except ValueError:
                    print("Sorry, please enter a valid decimal number.") #Prompts for user to enter a valid number by going back up
                    continue
                else:
                    print(DectoHex(int(enternumber)),"\nYour number has been converted. Please enter a new base for another number you want to convert, or type exit to leave")
                    return
        elif(option=="BINARY"):
            print("Please enter the base 10 number you want to convert or type 'Back' to choose a different option:")
            while True:
                enternumber = input().upper().strip()
                if enternumber == "EXIT":
                    ExitFunction()
                elif enternumber == "BACK":
                    break
                try:
                    enternumber = int(enternumber)  #Decimals are easy. Just check to see if it's an integer.
                except ValueError:
                    print("Sorry, please enter a valid decimal number.") #Prompts for user to enter a valid number by going back up
                    continue
                else:
                    print(RecursiveDectoBin(int(enternumber)),"\nYour number has been converted. Please enter a new base for another number you want to convert, or type exit to leave")
                    return
        elif(option=="BACK"):
            print("Choose to convert a decimal number, a binary number, or a hexadecimal number")
            return
        elif(option=="EXIT"):
            ExitFunction()
        else:
            print("Sorry, that's not one of the options.")

#Simple command-line based menu. Could have done a purely numerical one, but wanted to practice writen user input as well. Broken into submenu fuctions for readability and ease.
def Menu ():
    print("Welcome to the base converter!\nThis program can convert numbers between decimal, hexadecimal, and binary.\nFirst enter which of the three you want to convert. Don't worry, it's not case sensitive.\nAlternaively type 'Exit' at any time to leave") 
    while(True):
        selection = input().upper().strip() #Strip any trailing space before and after, and capitalize to not worry about case sensitivity.
        if(selection=="DECIMAL"):
            Decimal_Sub_Menu()
        elif (selection=="HEXADECIMAL"):
            Hexadecimal_Sub_Menu()
        elif (selection=="BINARY"):
            Binary_Sub_Menu()
            #pass
        elif selection == "EXIT":
            ExitFunction()
        else:
            print("Sorry, I didn't catch that. Please type 'Decimal', 'Binary' or 'Hexadecimal'")
    return
  
def main():
    Menu()
  
if __name__ == "__main__":
    main()
