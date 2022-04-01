#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 15:53:37 2019

@author: almaalvarado
"""

def print_board(board):
    print('- 0  1  2 ')
    d = 0 
    for r in board:
        print(d, end= "")
        d += 1
        for c in r:
            if c == 0:
               print("", end= " . ")
            elif c == 1:
               print(" X ", end= "")
            else:
               print(" O ", end= "")
        print()

def is_valid(r, c, board):
    #checking if the input is in the bounds of the board
    if r < 0 or r > 2:
        return False
    elif c < 0 or c > 2:
        return False
    elif board [r][c]==0:
        return True
    return False

def is_winner(board):
    #validating which player wins 
    if board[0][0] == board[0][1] == board [0][2] and board[0][0] != 0 and board [0][1] != 0 and board [0][2]:
        return True
    if board[1][0] == board[1][1]==board[1][2] and  board[1][0] != 0 and board [1][1] != 0 and board [1][2]:
        return True
    if board [2][0] == board[2][1]==board[2][2] and  board[2][0] != 0 and board [2][1] != 0 and board [2][2]:
        return True
    if board[0][2]==board[1][1]==board[2][0] and board[0][2] != 0 and board [1][1] != 0 and board [2][0]:
        return True
    if board [0][0] == board[1][1]==board[2][2] and  board[0][0] != 0 and board [1][1] != 0 and board [2][2]:
        return True
    if board [0][0] == board[1][0]==board[2][0] and  board[0][0] != 0 and board [1][0] != 0 and board [2][0]:
        return True
    if board [0][1] == board[1][1]==board[2][1] and  board[0][1] != 0 and board [1][1] != 0 and board [2][1]:
        return True
    if board [1][2] == board[2][2]==board[0][2] and  board[1][2] != 0 and board [2][2] != 0 and board [0][2]:
        return True
    return False

def main():       
    board=[
            [0,0,0],
            [0,0,0],
            [0,0,0]
           ]
    current = 1
    for i in range(9):
        #prints the board
        print_board(board)
        if is_winner(board)==True:
            break
        if current == 1:
            #let's the user know who's turn it is
            print("X's turn")
        else:
            print("O's turn")
        r=int(input("Give a row:"))
        c=int(input("Give a column:"))
        while not is_valid(r,c,board):
            r=int(input("Give a row:"))
            c=int(input("Give a column:"))
        board[r][c]= current
        if current == 1:
            current = 2
        else:
            current = 1
        
main()