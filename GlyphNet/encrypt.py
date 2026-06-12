emoji_map = {
        "a": "😀",
        "b": "😂",
        "c": "😎",
        "d": "🔥",
        "e": "🌟",
        "f": "🍀",
        "g": "🎯",
        "h": "🚀",
        "i": "💎",
        "j": "🎵",
        "k": "⚡",
        "l": "🌈",
        "m": "🧠",
        "n": "🐍",
        "o": "🌍",
        "p": "🍕",
        "q": "👑",
        "r": "🎮",
        "s": "🛡️",
        "t": "🌙",
        "u": "☀️",
        "v": "💥",
        "w": "🎲",
        "x": "❌",
        "y": "🪄",
        "z": "⚓",
    }

def  encrypt_text(text):
    result = ""

    for char in text.lower():
        if char == " ":
                result += "    "
        else :
                result += emoji_map.get(char , char ) + " "

    return result
