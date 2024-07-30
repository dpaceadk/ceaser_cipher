#importing OS module to check whether a file exists in folder
import os
def welcome():
    #Welcoming to the user
    print("Welcome to the Caesar Cipher")
    print("This program encrypts and decrypts text with the Caesar Cipher.")
    
def enter_message():
    #To choose between encrypting and decrypting
    check = True
    while check==True:
        choose = input("Would you like to encrypt (e) or decrypt (d): ")
        #loop where a boolean value is given and run the loop by giving the variable value check true
        if choose== "e":
            message = input("What message would you like to encrypt: ")
            check = False
        elif choose== "d":
            message = input("What message would you like to decrypt: ")
            check = False
        else:
            print("Invalid Mode!!!")
            choose = input("Would you like to encrypt (e) or decrypt (d): ")
        message = message.upper()
    value = True
    while value == True:
        try:
            shift = int(input("What is the shift number: ")) 
            value = False
        except ValueError:
            print("Invalid number!!!")
    return message, choose, shift

def encrypt(message,shift):
    #Function that coverts a given characeter into ASCII and gives the charcater of the given value 
    #Ecrypt moves the character forward
    encode = ""
    message= message.upper()
    for char in message:
        if char.isalpha():
            word = ((ord(char) + shift )) 
            if word > 90:
                word-=26
                new = chr(word)
            else:
                new = chr(word)
                encode+= new
        else:
            encode += char
        message = encode
    print(encode)
    return encode

def decrypt(message, shift):
    #Function that coverts a given characeter into ASCII and gives the charcater of the given value
    #Decrypt moves the character backward
    decode = ""
    message = message.upper()
    for char in message:
        if char.isalpha():
           word = ((ord(char) - shift))
           if word < 65:
               word +=26
               latest = chr(word)
           else:
               latest = chr(word)
           decode+=latest    
        else:
            decode+=char
        message = decode
    print(decode)
    return decode

def process_file(file_name, mode, shift):
    #To encrypt and decrypt a given character by reading the lines from the file
    try:
        with open(file_name,'r') as file:
            files = file.readlines()
            files = files.upper()
        mode = input("Would you like to encrypt (e) or decrypt (d): ")
        if mode == "e":
            encode = ""
            for message in files:
                if message.isalpha():
                    encode += chr(ord(message)+shift)
                else:
                    encode += message
            print(encode)
        elif mode == "d":
            decode= ""
            for message in files:
                if message.isalpha():
                    decode += chr(ord(message)-shift)
                else:
                    decode += message
            print(decode)
    except FileNotFoundError:
        #If error is found then this function displays the error
        print("File not found: ", file_name)    
        
def is_file(file_name):
    #To check whether a given files exists in a path or not
    file_name = input("Enter the file name: ")
    while True:
        try:
            if os.path.exists(file_name):
                return True
        except FileNotFoundError:
            return False 
        return file_name
   
def write_message(message):
    #wrting the charcters to the file result.txt
    with open("result_2358423.txt", 'w') as files:
        for string in message:
            files.write(string)
            
def message_or_file():
    #Asking users giving options to choose whether to read from a file or the console and encrypt or decrypt it
    valid = True
    while valid == True:
        #Looping to encrypt or decrypt
        mode = input("Would you like to encrypt (e) or decrypt(d): ")
        if mode == "e":
            message = input("Would you like to read from a file (f) or the console(c)? ")
            valid = False
        elif mode == "d":
            message = input("Would you like to read from a file (f) or the console(c)? ")
            valid = False
        else:
            print("Invalid mode!!!")
            mode = input("Would you like to encrypt (e) or decrypt(d): ")
            valid = True   
    desk = True
    while desk == True: 
        #looping to read from a file if the file exists if the command is f and encrypting or decrypting the value
        if message == "f":   
            while True:
                file_name = input("Enter a file name: ")
                try:
                   with open(file_name,'r') as red:
                    files = red.read()
                    files = files.upper()
                    shift = int(input("What is the shift number: ")) 
                    if mode == "d":
                        decode = ""
                        for char in files:
                            if char.isalpha():
                                word = ((ord(char) - shift))
                                if word < 65:
                                    word +=26
                                    latest = chr(word)
                                else:
                                    latest = chr(word)
                                decode+=latest    
                            else:
                                decode+=char
                            message = decode
                        with open("result_2358423.txt", 'w') as file:
                            done = file.write(decode)
                        print(decode)
                        return decode
                    elif mode == "e":
                        encode = ""
                        for char in files:
                            if char.isalpha():
                                word = ((ord(char) + shift))
                                if word > 90:
                                    word -=26
                                    latest = chr(word)
                                else:
                                    latest = chr(word)
                                encode+=latest    
                            else:
                                encode+=char
                            message = encode
                        with open("result_2358423.txt", 'w') as file:
                            done = file.write(encode)
                        print(encode)   
                        return encode
                    False
                    return mode, None, file_name
                except FileNotFoundError:
                    print("Invalid File Name")
                    file_name = input("Enter a file name: ")
                    True
        else: 
            #if the mode is command and converts the value according to the mode
            left = input(f"What message would you like to {mode}: ".format({message})).upper()
            shift = int(input("What is the shift number: ")) 
            if mode == "d":
                decode = ""
                for char in left:
                    if char.isalpha():
                        word = ((ord(char) - shift))
                        if word < 65:
                            word +=26
                            latest = chr(word)
                        else:
                            latest = chr(word)
                        decode+=latest    
                    else:
                        decode+=char
                    message = decode
                print(decode)
                return decode
            elif mode == "e":
                encode = ""
                for char in left:
                    if char.isalpha():
                        word = ((ord(char) + shift))
                        if word > 90:
                            word -=26
                            latest = chr(word)
                        else:
                            latest = chr(word)
                        encode+=latest    
                    else:
                        encode+=char
                    message = encode
                print(encode)   
                return encode  
        desk = False #to end the loop giving the variable value False
    return mode, message, shift

def main():
    #Combinig all the functions 
    welcome()
    while True:
        #looping if the user wants to continue to encrypt or decrypt the character...
        message_or_file()
        message = input("Would you like to encrypt or decrypt another message? (y/n): ")
        if message != "y" and message!="n":
            print("Invalid syntax!!")
            message = input("Would you like to encrypt or decrypt another message? (y/n): ")
        elif message == "n":
            #if the user enters n then displaying thank you message and break the loop
            print("Thank you for using the program, goodbye!!")
            break
main()