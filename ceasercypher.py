import random
import math


logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

Game = True
print(logo, "\n Welcome to Ceaser Cipher!!! \n")
while Game == True:
    text = input("Type the message:\n").lower()
    direction = input("Do you want to Encrypte (>) or Decrpyte (<): \n")
    shift = int(input("Type the number you want to shift by:\n"))
    



    def ceaser(text, shift, direction):
    

        Coded_Word = ""
        for letters in text:
            position = alphabet.index(letters)
            if direction == ">":
                Coded_Word += alphabet[position + shift]
            elif direction == "<":
                Coded_Word +=  alphabet[position - shift]
            else:
                print("Wrong direction \n")
                
        print(Coded_Word)
                
        
        
                                    

    ceaser(text, shift, direction)
    
    again = input("Do you want to continue? ('yes' or 'no') \n")

    if again == "no":
        print("!!!GOODBYE!!!")
        Game = False