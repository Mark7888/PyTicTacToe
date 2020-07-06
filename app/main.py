import os
#import discord
from colorama import init
from colorama import Fore, Back, Style
from configparser import ConfigParser
init(autoreset=True)
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
#client = DiscordClient()
config = ConfigParser()
cls()
def lines(num1, num2, num3, val1, val2, val3):
    line = """
    ┌""" + num1 + """─────┐┌""" + num2 + """─────┐┌""" + num3 + """─────┐
    │  """ + val1 + """  ││  """ + val2 + """  ││  """ + val3 + """  │
    │  """ + val1 + """  ││  """ + val2 + """  ││  """ + val3 + """  │
    └───────┘└───────┘└───────┘"""
    return(line)

line1 = lines("A1", "B1", "C1", "   ", "   ", "   ")
line2 = lines("A2", "B2", "C2", "   ", "   ", "   ")
line3 = lines("A3", "B3", "C3", "   ", "   ", "   ")
board = line1 + line2 + line3
print(board)
