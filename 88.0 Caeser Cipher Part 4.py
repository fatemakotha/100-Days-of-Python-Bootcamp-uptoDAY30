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


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction): #.....8
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
    
  for char in start_text:
    if char in alphabet: #checkes if the char is a letter or anything else like a number or a symbol
        position = alphabet.index(char)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    else:
        end_text += char
    
  print(f"Here's the {cipher_direction}d result: {end_text}")

print(logo)

should_continue = True #.....1
while should_continue: #.....2
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n") #.....3
    text = input("Type your message:\n").lower() #.....4
    shift = int(input("Type the shift number:\n")) #.....5
    
    shift = shift % 25 #25 is the number of letters in the list of alphabets #.....6
                       #if shift is 59, then 
                    #   59 / 25 = 2.36
                    #   2 x 25 = 50
                    #   59 - 50 = 9 *** shift is now 9 
    
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction) #.....7
    
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n")
    
    if result == "no":
        should_continue = False
        print("Goodbye")
    