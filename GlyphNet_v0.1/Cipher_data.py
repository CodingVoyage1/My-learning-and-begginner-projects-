import random


cipher = {
    "a": ["😀", "👋", "🥭"],
    "b": ["🥝","🧨","🧤"],
    "c": ["🚰", "🫠", "🏔️"]

}

def cipher_d (text):
    result = " "
    for char in text:
        if char == " ":
            result += " "
        else :
            result += random.choice(cipher[char])
    return result

text = input("Enter the Text :")
encrypted_text = cipher_d(text)
print("Encrypted Text :", encrypted_text)