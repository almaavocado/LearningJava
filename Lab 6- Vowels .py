#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 10:39:27 2019

@author: almaalvarado
"""

def get_word():
    #no parameters and returns a string
    user_word = input("Please enter a word:")
    return user_word

def is_vowel(letter):
    #parameters: letter and returns True/False
    if letter =='a' or letter == 'e' or letter == 'i' or letter =='o' or letter == 'u':
        #defining what letters are vowels
        return True
    else:
        return False
        
def calculate(user_word):
    #parameters: word as a string and returns a integer(measure)
    switch=0
    #the switch is off to see if there is a constant before a vowel
    count=0
    #we are counting the measure of the string
    for i in range(len(user_word)):
        check_vowel = is_vowel(user_word[i])
        #we are checking each letter of the word the user gave us
        if check_vowel == True and switch == 1:
            #we are turning the switch on if we have a consonant
            switch = 0
            count = count + 1
            #the count is increamenting by one if we have a consonant and a vowel 
        if check_vowel == False and switch == 0:
            #the switch is turning on if we have a both a no wel and consonant 
            switch = 1
    return count
#this will return the measure of the word

def main():
    #this main function will drive the program
    print (calculate(get_word()))

main()
#calling on the main function to run the program 