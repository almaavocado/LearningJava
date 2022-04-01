#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 11:11:07 2019

@author: almaalvarado
"""

print("Welcome to the V/C Counter!")

#Make List
vowels = list("aeiouy")
consonants = list("bcdfghjklmnpqrstvexz")

complete = False
while complete == False:
    mode = input("What mode would you like? Vowels or Consonants?: ").lower().strip()
    print("")
    print("You chose the mode: " + str(mode))
    print("")
    if mode == "vowels":
        word = input("Please input a word: ")
        print("your word was: " + str(word))
        print("")



        choice = input("Are you done, Y/N: ").lower().strip()
        if choice == "y":
            complete = True
        else:
            print("Ok, back to the top!")
    elif mode == "consonants":
        word = input("please input a word: ")
        print("your word was: " + str(word))
        print("")


        choice = input("Are you done, Y/N: ").lower().strip()
        if choice == "y":
            complete = True
        else:
            print("Ok, back to the top!")
    else:
        print("Improper Mode, please input a correct one")

print("Thank you for using this program")
