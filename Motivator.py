"""
Docstring for fortuneTeller
So its basically a programme where you enter a random as your lucky and according to that 
you will get your Motivation boost up Quotes,  it also has a progress bar(just to make it look better )
"""


import random as rnd 
from tqdm import tqdm as t 
import time 

for i in t(range(100), desc="Processing", ncols=100,colour="yellow"):
    time.sleep(0.02)

response = int(input("Enter your lucky number  :"))

yourLucks = [
    "You are going to be bigger this year ",
    "you are mature ",
    "you are going to have GF",
    "you are going to get a job ",
    "you are making progress in the things you are doing",
    "be happy ",
    "You are lucky this year ",
    "Be better this year ",
    "Work harder this year ",
    'You will get lots of money ',
    "You will work in Goggle this year ",
    "Work on yourself ",
    "Chase your goals ",
    "Dont chase girls , chase your ambition",
    "Code everyday , even for 10min ",
    "Consistency works like magic . Be consistence",
    "Ai not gonna take over ",
    

]

if response in range(0, 100):
    sfl = rnd.choice(yourLucks)
    print(sfl)

else:
    print("invalid input ")