from unittest import result

from encrypt import emoji_map


reverse_map = {}

for key, value in emoji_map.items():
    reverse_map[value] = key

def decrypt_text(text):
    result = ""

    emojis = text.split()
    for emoji in emojis:
        result += reverse_map.get(emoji, emoji)
    return result