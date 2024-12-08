import random
letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['@','#','$','%','&','(',')','*','+','.']
print("Welcome to password generator!")

no_letters=int(input("How many letters do you want? "))
no_numbers=int(input("How many numbers do you want? "))
no_symbols=int(input("How many symbols do you want? "))

password_list=[]
for i in range(1,no_letters+1):
    char=random.choice(letters)
    password_list+=char
for i in range(1,no_numbers+1):
    char=random.choice(numbers)
    password_list+=char
for i in range(1,no_symbols+1):
    char=random.choice(symbols)
    password_list+=char
print(password_list)

random.shuffle(password_list)
print(password_list)

password=''
for j in password_list:
    password+=j
print(password)