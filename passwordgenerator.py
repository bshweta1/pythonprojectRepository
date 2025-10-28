import random

letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',  'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols=['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

print("Welcome to password generator!")
nlttr=int(input("How many letters would you like in your password"))
nnum=int(input("how many number would you like in your password"))
nsymbl=int(input("how many symbols would you like in your password?"))
npswrd=nlttr-(nnum+nsymbl)


password_list=[]
for char in range(0,npswrd):
    password_list.append( random.choice(letters))
for char in range(0,nnum):
    password_list.append(random.choice(numbers))
for char in range(0,nsymbl):
    password_list.append(random.choice(symbols))
    random.shuffle(password_list)
    # print(password_list)
password=""
for char in password_list:
    password+= char
print(f"your password is:{password}")