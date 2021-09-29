from random import randint
from termcolor import colored as c

resultsFileName = "results.txt"

def genDice(numDice):
  dice = []
  
  for _ in range(numDice):
    dice.append(randint(1, 6))  
  
  tot = sum(dice[0:numDice])
  resultsFile = open(resultsFileName, "a")
  resultsFile.write(f"{tot}\n")

def clearFile():
  resultsFile = open(resultsFileName, "w")
  resultsFile.write("")

def countNums():
  resultsFile = open(resultsFileName, "r")
  results = resultsFile.read().split("\n")
  freq = {}
  for _ in results:
    if _ in freq:
      freq[_] += 1
    else:
      freq[_] = 1
  res = max(freq, key = freq.get)
  return f"{res}"

title = """  ____               ██████╗ ██╗ ██████╗███████╗    ██████╗  ██████╗ ██╗     ██╗     ███████╗██████╗ 
 /\\' .\    _____     ██╔══██╗██║██╔════╝██╔════╝    ██╔══██╗██╔═══██╗██║     ██║     ██╔════╝██╔══██╗
/: \___\  / .  /\\    ██║  ██║██║██║     █████╗      ██████╔╝██║   ██║██║     ██║     █████╗  ██████╔╝
\\' / . / /____/..\\   ██║  ██║██║██║     ██╔══╝      ██╔══██╗██║   ██║██║     ██║     ██╔══╝  ██╔══██╗
 \\/___/  \\'  '\  /   ██████╔╝██║╚██████╗███████╗    ██║  ██║╚██████╔╝███████╗███████╗███████╗██║  ██║
          \\'__'\/    ╚═════╝ ╚═╝ ╚═════╝╚══════╝    ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝"""
title = title.split("\n")
print(c(title[0],"red"))
print(c(title[1],"yellow"))
print(c(title[2],"green"))
print(c(title[3],"cyan"))
print(c(title[4],"blue"))
print(c(title[5],"magenta"))

clearFile()

NUM_DICE = int(input("\nInput how many dice you want to roll (1-100): "))
NUM_SIMS = int(input("How many times do you want to simulate? (higher = more accurate): "))
DO_PRINT = input("Do you want to print the number of dice rolled? (Y/n): ")

for _ in range(NUM_SIMS):
  if(DO_PRINT.lower() in ["yes", "ye", "y"]):
    print(f"{_+1}/{NUM_SIMS} dice rolled... ({(_+1)/NUM_SIMS*100}%)")
    genDice(NUM_DICE)
  else:
    genDice(NUM_DICE)

print(f'\nThe most common number is: {countNums()}')