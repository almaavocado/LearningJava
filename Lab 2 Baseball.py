#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 10:37:15 2019

@author: almaalvarado
"""

player_name =input("Please enter the players full name: ")
plate_apperance =input("Please enter the number of times a player takes a turn batting:")
at_bats =input("Please enter the number of plate appreances that do not result in a walk, a hit by a pitch, or a sacrafice fly or blunt:")
walks =input("Please enter the number of plate apperances that result in a freewalk:" )
single = eval(input("Please enter the number of hits that are a single (batter ends up on first base):"))
doubles = eval(input("Please enter the number of hits that are double (batter ends up on second base):"))
triples = eval(input("Please enter the number of hits that are a triple (batter ends up on third base):"))
homeruns = eval(input("Please enter the number of home run hits:"))
#Input functions will determine total hits, batting average, slugging percentage, and On-base slugging

total_bases = (int(single)) + (int(doubles*2)) + (int(triples*3)) + (int(homeruns*4))
#This function will calculate the total amount of bases 

total_hits = int(single) + int(doubles) + int(triples) + int(homeruns)
#This function will determine the total number of hits
print("This is the player's total number of hits:" ,total_hits)
#This print function will display the total number of hits to the user

batting_avg = int(total_hits)/int(at_bats)
#This function will find the players batting average
print( "This is the player's batting average:" "{0: .3f}" .format(batting_avg))
#This print function will display the players batting average (rounded to the nearest thousand)

OBP = (int(total_hits) + int(walks))/(int(plate_apperance))
#This function will calculate the on base percentage

#This function will calculate the total amount of bases 

slugging_percent = (int(total_bases)/int(at_bats))
#This function will calculate the player's slugging percentage
print("This is the player's slugging percentage:" "{0: .3f}" .format(slugging_percent))
#This print function will display the players slugging percentage (rounded to the nearest thousand)

OPS = (float(OBP) + float(slugging_percent))
#This function will calculate the player's On Base Plus Slugging percentage
print("This is the player's On-base Plus Slugging:" "{0: .3f}" .format(OPS))
#This print function will display the player's On Base Plus Slugging percentage (rounded to the nearest thousand)

#Research Questions:
#Babe Ruth has the all-time highest career OPS stats of 1.1636
#Mike Trout has the highest career OPS stats among active playes at 0.9897