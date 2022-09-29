# import random module 
import random

# user input password legnth 
passlen = int(input("Enter Password Length : "))

# storing letters, numbers, special characters
s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

# random sampling by joining the length of password and the variable s
p = "".join(random.sample(s,passlen))
print(p)
