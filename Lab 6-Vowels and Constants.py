#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 10:35:18 2019

@author: almaalvarado
"""

def got_word():
    #no parameters and returns a string
    user_word = input("Please enter a word:")
    return user_word

def is_vowel(letter):
    #parameters: letter and returns True/False
    for i in range(len(user_word)):
        if user_word[i]=="a" and user_word[i]== "e" and user_word[i]== "i" and user_word[i]== "o" and user_word[i]=="u":
            return True
        else:
            return False
        
def calculate(user_word):
    #parameters: word as a string and returns a integer(measure)
    save_first = str[0]
    return user_word

def main():
    