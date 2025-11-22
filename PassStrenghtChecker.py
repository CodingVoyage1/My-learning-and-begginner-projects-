#Password strength checker
import re

def check_pass_strength(password):
    strength = 0

    if len(password) < 8:
        return 'Password must be at least 8 chars long'
    else:
        strength = strength + 1

    if re.search('[a-z]', password):
        strength = strength + 1

    if re.search('[A-Z]', password):
        strength = strength + 1

    if re.search('[0-9]', password):
        strength = strength + 1

    if re.search('[!@#$%^&*(),.?":]', password):
        strength = strength + 1

    if strength == 5:
        return 'Your password is strong'
    elif strength >= 3:
        return 'Your password is moderate'
    else:
        return 'Your password is weak'

def inputs():
    while True:
        password_input = input('Enter your password to check its strength (or type "exit" to quit): ')
        if password_input.lower() == "exit":
            return 'Thanks for using the password strength checker'
            break

        result = check_pass_strength(password_input)
        print(result)

if __name__ == "__main__":
    inputs()

 
