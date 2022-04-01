# We can write a "menu" in a program using an if-elif-elif-else structure.

print("Which of the Seven New Gods would you like to learn about?")
print("1. The Father")
print("2. The Mother")
print("3. The Maiden")
print("4. The Crone")
print("5. The Warrior")
print("6. The Smith")
print("7. The Stranger")

# Read the user's input in response to the menu.
selection = int(input())

# Select an appropriate action.
if selection == 1:
    print("The Father represents divine justice, and judges the souls of the dead.")
elif selection == 2:
    print("The Mother represents mercy, peace, fertility, and childbirth. She is sometimes referred to as \"the strength of women\".")
elif selection == 3:
    print("The Maiden represents purity, innocence, love, and beauty.")
elif selection == 4:
    print("The Crone represents wisdom and foresight. She is represented carrying a lantern.")
elif selection == 5:
    print("The Warrior represents strength and courage in battle.")
elif selection == 6:
    print("The Smith represents creation and craftsmanship.")
elif selection == 7:
    print("The Stranger represents death and the unknown. It is rarely prayed to.")
elif selection == 0:
    print("Valar morghulis.")
# The final else is a "none of the other options was chosen" branch.
else:
    print("The night is dark and full of terrors for those who cannot read the menu.")
