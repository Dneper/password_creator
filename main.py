import random 
symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password_length = int(input('какая длинна пароля вам нужна?'))

password = ''

for i in range(password_length):
    password += random.choice(symbols)

print(password)
    
