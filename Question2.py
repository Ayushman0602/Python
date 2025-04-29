
import random
a = "abcdefghijklmnopqrstuvwxyz"
b = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
c = "0123456789"
d = "!@#$%^&*()"
x = a+b+c+d
y = int(input("Enter the length of password you want to create: "))
password = "".join(random.sample(x , y))
print(f"Your passwprd is: \n{password}")