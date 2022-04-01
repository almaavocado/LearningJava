#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 10:47:52 2019

@author: almaalvarado
"""

def get_magnitude(number):
    magnitude = float(input("Please enter the magnitude of earthquake " +number+":"))
    #Getting magnitude from the user
    while magnitude <= 0:
        #this will force the user to insert a positive number as magnitude
        magnitude = float(input("Please enter the magnitude of earthquake " +number+":"))
    return magnitude

def compare_magnitudes(magnitude1, magnitude2):
    #this define function assumes that magnitude1 is greater than magnitude2
    earth_mag = 10**(1.5*(magnitude1-magnitude2))
    return earth_mag
    
def get_run_again():
    #this will ask the user if they wish to run the program again 
    run_again = int(input("Would you like to run this program again? Enter 1 if yes:"))
    if run_again == 1:
        #if run again is equal to one it will return True so that you can use it to loop later on
        return True
    else:
        return False
    
def main():
    run_again = 1
    #setting run again to the only good value (1) so that it will enter the loop. 
    while run_again == 1:
        magnitude1 = get_magnitude(("1"))
        #this will ask the user to input the magnitude from the 1st earthquake
        magnitude2 = get_magnitude(("2"))
        #this will ask the user to input the magnitude from the 2nd earthquake
        if magnitude1 > magnitude2:
            #this is where the program will determine whether magnitude1 is bigger than magnitude2
            compare_magnitudes(magnitude1, magnitude2)
            earth_mag=compare_magnitudes(magnitude1, magnitude2)
            print("An earthquake of magnitude",magnitude1, "is", "{0: .1f}".format(earth_mag), "times more powerful than an earthquake of magnitude",magnitude2)
        else:
            #this is where the program will determine whether magnitude2 is bigger than magnitude1
            #since the define function assumes magnitude1 is greater than magnitude2 we have to change the parameters to make 
            #magnitude2 greater than magnitude1 and replace the parameters in the def compare_magnitudes statement 
            compare_magnitudes(magnitude2, magnitude1)
            earth_mag=compare_magnitudes(magnitude2, magnitude1)
            print("An earthquake of magnitude",magnitude2, "is","{0: .1f}".format(earth_mag), "times more powerful than an earthquake of magnitude",magnitude1)
        #this will break the loop asking the user to re run the program
        run_again = get_run_again()
    print("Thank You. Bye!")
main()
#this will call on the def main to complete all the functions    
#Research Questions:
    #1. (a) Magnitude of 2011 Tohoku earthquake, Japan was 9.1 Mw
    #(b). Magnitude of 1989 Loma Prieta earthquake, San Francisco, USA was 6.9 Mw
    #(c). Magnitude of 2010 Haiti earthquake was 7.0 Mw
    
    #2. 1412.5 times more powerful
    
    #3. 230,000(Haiti) and 15,894(Tohoku): Yes I appreciate modern technology