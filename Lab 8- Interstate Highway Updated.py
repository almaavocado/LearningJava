#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 11:14:49 2019

@author: almaalvarado
"""

def get_interstate_number():
    user_choice_highway = input('Please enter a US Interstate Highway route number: ')
    if user_choice_highway.startswith('I-'):
        highway = user_choice_highway[2:]
       #this will give highway the int only 
    elif user_choice_highway[0:11] == 'Interstate ':
        highway = user_choice_highway[11:]  
        #this will give highway the number only leaving out the letters
               
    elif user_choice_highway[0] == 'I':
        highway = user_choice_highway[1:]
        #if the first character of the string is 'I'
        
    else:
        highway = user_choice_highway
        #the code will get here if the user inputs a number
        
    return int(highway)

def is_primary(number):
    if number <= 99:
        #this will check if the numbers are one/two-didgit numbers
        return True
    else:
        return False

def compass_orientation(number):
    #we are checking if the interstate is even or odd numbered 
    if number % 2 == 1:
        return 'North-South'
    if number % 2 == 0:
        return 'East-West'

def is_arterial(number):
    #this function also can only be called on a primary interstate number
    if number % 5 == 0:
        return True
    else:
        return False
    
def auxiliary_type(number):
   #this function can only be called on an auxiliary interstate number, and returns the type of auxilary highway 
    if (number // 100) % 2 == 1:
        return 'Spur'
    elif (number // 100) % 2 == 0:
        return 'Radical'
    
def parent_highway(number):
    #this function will be called on to see if the highway is a parent highway
    parent_way = number - (number // 100)*100
    return parent_way

def main():
    #this main fucntion drives the entire program
    number = get_interstate_number()
    primary_way = is_primary(number)
    if primary_way == True:
        compass_way = compass_orientation(number)
        arterial_way = is_arterial(number)
        if arterial_way == True:
            #this will determine if the highway is long distance arterial and what orientation the highway is
            print("Interstate", number, "is a long distance arterial highway oriented", compass_way)
        elif arterial_way == False:
            print("Insterstate", number, "is oriented",compass_way)
    elif primary_way == False:
        #this will determine if it is a spur or radical highway
        auxiliary_way = auxiliary_type(number)
        parent_ways = parent_highway(number)
        print("Interstate",number, "is a", auxiliary_way, "highway of Interstate", parent_ways)
        
            
main()