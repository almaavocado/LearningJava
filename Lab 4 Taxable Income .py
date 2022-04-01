#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 10:13:59 2019

@author: almaalvarado
"""
#defining the variables value to avoid having too many numbers in the equations needed to calulate liability and effective tax rate.
tax_owed12 = 952.50
tax_owed22 = 4453.50
tax_owed24 = 14089.50
tax_owed32 = 32089.50
tax_owed35 = 45689.50
tax_owed37 = 150689.50
tax_owed70 = 3665689.50

#Introducing the program to the user (user friendly) and stating the purpose of the program.
print("Welcome to your tax calculator. This will only work if you file your taxes as single.")
income_2018 = int(input("Please enter your total income for 2018. (in whole dollar amounts) $"))
if income_2018>=0 and income_2018<=9525:
#The user will fall into this category if their income is less than 9525 and will let them know the reasoning behind the calculations. 
    print("You will need to pay 10% of taxable income. Please find the calculations below.")
    tax_liability = (income_2018) * .10
    print("Your tax liability is", "$""{0:.2f}".format(tax_liability))
#Formating how the user will see their tax liability with a dollar sign and rounded.
    effective_rate = (tax_liability/income_2018) * 100
    print("Your effetive tax rate is","{0:.1f}".format(effective_rate)+"%")
 #Formating how the user will see their effective tax rate with a dollar sign and rounded.   
if income_2018>=9526 and income_2018<=38700:
#The user will fall into this category if their income is between 9526 and 38700
    print("You will need to pay $952.50 plus 12% of the amount over $9,525. Please find the calculations below.")
    tax_liability = (tax_owed12) + ((income_2018 - 9525) * 0.12)
    print("Your tax liability is", "$""{0:.2f}".format(tax_liability))
#Formating how the user will see their tax liability with a dollar sign and rounded.
    effective_rate = (tax_liability/income_2018) * 100
    print("Your effetive tax rate is","{0:.1f}".format(effective_rate)+"%")
 #Formating how the user will see their effective tax rate with a dollar sign and rounded.   

if income_2018>=38701 and income_2018<=82500:
#The user will fall into this category if their income is between 38701 and 82500.
    print("You will need to pay $4,453.50 plus 22% of the amount over $38,700. Please find the calculations below.")
    tax_liability = (tax_owed22) + ((income_2018 - 38700)* 0.22)
    print("Your tax liability is", "$""{0:.2f}".format(tax_liability))
#Formating how the user will see their tax liability with a dollar sign and rounded.
    effective_rate = (tax_liability/income_2018) * 100
    print("Your effetive tax rate is","{0:.1f}".format(effective_rate)+"%")
 #Formating how the user will see their effective tax rate with a dollar sign and rounded.   

if income_2018>=82501 and income_2018<=157500:
#The user will fall into this category if their income is between 82501 and 157500. 
    print("You will need to pay $14,089.50 plus 24% of the amount over $82,500. Please find the calculations below.")
    tax_liability = (tax_owed24) + ((income_2018 - 85000) * 0.24)
    print("Your tax liability is", "$""{0:.2f}".format(tax_liability))
#Formating how the user will see their tax liability with a dollar sign and rounded.
    effective_rate = (tax_liability/income_2018) * 100
    print("Your effetive tax rate is","{0:.1f}".format(effective_rate)+"%")

if income_2018>=157501 and income_2018<=200000:
#The user will fall into this category if their income is between 157501 and 200000
    print("You will need to pay $32,089.50 plus 32% of the amount over $157,500. Please find the calculations below.")
    tax_liability = (tax_owed32) +((income_2018 - 157500) * 0.32)
    print("Your tax liability is", "$""{0:.2f}".format(tax_liability))
#Formating how the user will see their tax liability with a dollar sign and rounded.
    effective_rate = (tax_liability/income_2018) *100
    print("Your effetive tax rate is","{0:.1f}".format(effective_rate)+"%")
 #Formating how the user will see their effective tax rate with a dollar sign and rounded.   

if income_2018>=2000001 and income_2018<=500000:
#The user will fall into this category if their income is between 2000001 and 500000
    print("You will need to pay $45,689.50 plus 35% of the amount over $200,000. Please find the calculations below.")
    tax_liability = (tax_owed35) + ((income_2018 - 200000) * 0.35)
    print("Your tax liability is", "$""{0:.2f}".format(tax_liability))
#Formating how the user will see their tax liability with a dollar sign and rounded.
    effective_rate = (tax_liability/income_2018) *100
    print("Your effetive tax rate is","{0:.1f}".format(effective_rate)+"%")
 #Formating how the user will see their effective tax rate with a dollar sign and rounded.   

if income_2018>=500001:
#The user will fall into this category if their income is greater than or equal to 500001
    print("You will need to pay $150,689.50 plus 37% of the amount over $500,000. Please find the calculations below.")
    tax_liability = (tax_owed37) + ((income_2018 - 500000) * 0.37)
    print("Your tax liability is", "$""{0:.2f}".format(tax_liability))
#Formating how the user will see their tax liability with a dollar sign and rounded.
    effective_rate = (tax_liability/income_2018) * 100
    print("Your effetive tax rate is","{0:.1f}".format(effective_rate)+"%")
 #Formating how the user will see their effective tax rate with a dollar sign and rounded.   

if income_2018 >= 10000001:
#The user will fall into this category if their income is greater than or equal to 10000001
    tax_liability = (tax_owed70) + ((income_2018 - 10000000) * 0.70)
    tax_liability = tax_liability // 1 + 0.50
    effective_rate = (tax_liability/income_2018) * 100
    print("With a braket set at 70%,")  
    print("Your tax liability is", "$""{0:.2f}".format(tax_liability))
#Formating how the user will see their tax liability with a dollar sign and rounded.
    print("Your effetive tax rate is","{0:.1f}".format(effective_rate)+"%")
 #Formating how the user will see their effective tax rate with a dollar sign and rounded.   
 
 #According to Glassdoor.com the mean (average) salary for a Software Engineer living in the Los Angeles, CA area is $100,614
 #The salary above is one percent of the $10,000,000
 #If I'd had to guess I would say 1 person in the class will make an income more that $10,000,000
    