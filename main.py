#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
letter_str=''
for i in range (1,nr_letters+1):
  rand_letter=random.randint(0,len(letters)-1)
  letter_str+=letters[rand_letter]

symbol_str=''
for i in range (1,nr_symbols+1):
  rand_sym=random.randint(0,len(symbols)-1)
  symbol_str+=symbols[rand_sym]

number_str=''
for i in range (1,nr_numbers+1):
  rand_num=random.randint(0,len(numbers)-1)
  number_str+=numbers[rand_num]

print(f"{symbol_str}{number_str}{letter_str}")
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_str=[]
for i in range (0,nr_letters):
  rand_letter=random.randint(0,len(letters)-1)
  password_str.append(letters[rand_letter])

for i in range (0,nr_symbols):
  rand_sym=random.randint(0,len(symbols)-1)
  password_str.append(symbols[rand_sym])

for i in range (1,nr_numbers+1):
  rand_num=random.randint(0,len(numbers)-1)
  password_str.append(numbers[rand_num])

final_pass=''
for i in range(0,len(password_str)-1):
  final_pass+=password_str[random.randint(0,len(password_str)-1)]

print(final_pass)
