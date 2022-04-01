#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 11:04:36 2019

@author: almaalvarado
"""

def main():
    placings = ["Sweden", "South Korea", "Japan", "Great Britian", "China", "Canada", "Switzerland", "United States", "Russia", "Denmark"]
    #listing the countries who placed in the order they placed
    country_choice = ""
    #setting country choice to an emty string to enter the loop where they are inputing a country
    
    while country_choice != "quit":
        #this loop will continue unless the user inputs "quit"
        country_choice = input("Please enter a country from the Women's 2018 Curling Olymics or 'quit':")
        
        if country_choice == "quit":
            print("Bye! Thank You.")
            break
        #this will end the program since the user input was "quit"
        place = 11
        for i in range(len(placings)):
            #this for loop will check if the country the user will input is in the list
            if placings[i]==country_choice:
                place = i
                
        if place == 0:
            print(country_choice, "placed 1st place earning a gold medal.")
            
        elif place == 1:
            print(country_choice, "placed 2nd place earning a silver medal.")
            
        elif place == 2:
            print(country_choice, "placed 3rd place earning a bronze medal.")
            
        elif place == 11:
            print(country_choice, "did not compete in the 2018 Olympics for Women's curling")
            #this will let the user know that they did not compete because the country is not in the list
        else:
            print(country_choice, "placed", place + 1)
        #this will add a number to their place in the list giving the user their correct placing
            
main()

#Research Questions
#1. Defi􏰂ne the following terms from the sport of curling: 
#(a) Stone: is made of granite and is specified by the World Curling Federation
#(b) House:The rings or circles toward which play is directed consisting of a 12-foot ring, 8-foot ring, 4-foot ring and a button. 
#(c) Button: The circle at the centre of the house.
#(d) Sweeper: The action of moving a broom or brush back and forth in the path of a moving stone.
#(e) Skip: The player who determines the strategy, and directs play for the team. The skip delivers the last pair of stones for his/her team in each end.

#2. What nation has won the most all-time total medals in the Winter Olympic Games?
#Norway
#3. What is the only winter sport that the United States has never earned an Olympic medal in?
#Biathlon