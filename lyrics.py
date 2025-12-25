import time 
import sys

print("----------CodingVoyage---------\n\n\n")
print("---------Last leaves Of Autumn-------")
print("Lyrics:")

def lyrics_p():

    lyrics = [
        "I give my heart away for another day",
        "In her cold embrace, but I'm anxious",
        "No matter what I say, she just pulls away",
        "Summer turns to rain in a heartbeat\n",
        "Now she's falling",
        "Falling like the last leaves of autumn",
        "So cold (so cold), so cold, and",
        "I can't find a way to bring her home",
        "'Cause my love keeps falling"
    ]

    delays_in = [
        0.3, 0.3, 0.4, 0.3, 0.3, 0.3, 0.8,
    ]

    time.sleep(1.2)

    for i, line in enumerate(lyrics):
        for char in line :
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.07)
        print()
        if i < len(delays_in):
            time.sleep(delays_in[i])
        else:
            time.sleep(0.8)
lyrics_p()