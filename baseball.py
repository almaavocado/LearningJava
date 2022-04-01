#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 16:12:58 2019

@author: almaalvarado
"""

# Write these functions:

# read_players -- returns a list of player tuples
# print_player -- given a player tuple, print that player's information
# find_player -- given a list of players and a name, returns the tuple for the
#   player with the given name
# find_highest_avg -- given a list of players, returns the tuple for the player
#   with the highest batting average (AVG)

def read_players(file_name):
    result = []

    first_line = True
    
    for line in open(file_name):
        if first_line:
            first_line = False
            continue
        
        # read: Name=0, Team=1, AB=3, HR=9
        split_line = line.split(",")
        # strip('"')
        
        player = (split_line[0].strip('"'), split_line[1].strip('"'),\
                  int(split_line[3].strip('"')), int(split_line[9].strip('"')))
        result.append(player)

    return result

def main():
    all_players = read_players("baseball_players.csv")
    choice = 0
    while choice != 4:
        print("1. Search for player")
        print("2. Search for team")
        print("3. Find max homeruns")
        print("4. Quit")

        choice = int(input("Enter a choice: "))
        if choice == 1:
            search_for_player(all_players)
        elif choice == 2:
            search_for_team(all_players)
        elif choice == 3:
            find_max_hrs(all_players)

def print_player(player):
    (name, team, ab, hr) = player
    print("{0} ({1}): {2} AB, {3} HR".format(name, team, ab, hr))

def find_max_hrs(all_players):
    max_hrs = all_players[0][3]
    max_player = all_players[0]
    for player in all_players:
        (name, team, ab, hr) = player
        if hr > max_hrs:
            max_player = player
            max_hrs = hr
    print_player(max_player)

def search_for_team(all_players):
    # Ask the user to type in a team name
    # Iterate through all the players
    # When you find a player on the team that the user input,
    search_name=input("Please enter a team's nameL")

    for player in all_players:
        (name,team,ab,hr)=player
        if team == search_name:
            print_player(player)

def search_for_player(all_players):
    search_name = input("Please enter a player's name:")

    for player in all_players:
        (name, team, ab, hr) = player
        if name == search_name:
            print_player(player)
            break
        
    
main()

