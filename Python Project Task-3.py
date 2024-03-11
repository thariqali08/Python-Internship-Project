import random
import string


#get the lenth of password
pwd_len=int(input("Enter the password length:"))

#assign password data
lower_letter=string.ascii_lowercase
upper_letter=string.ascii_uppercase
digit=string.digits
spl_char=string.punctuation

#combine all data
all=lower_letter + upper_letter + digit + spl_char

#use random
temp=random.sample(all,pwd_len)

#generate password
pwd="".join(temp)
print("Generate Password:",pwd)
