#RANDOM PASSWORD GENERATOR

import random
import string

alpha1 = string.ascii_lowercase
alpha2 = string.ascii_uppercase
num = string.digits
alpha3 = string.punctuation

password_length = int(input('enter your password length:'))


s = []
s.extend(alpha1)
s.extend(alpha2)
s.extend(alpha3)
s.extend(num)
print('your password is :')
print(''.join(random.sample(s, password_length)))








