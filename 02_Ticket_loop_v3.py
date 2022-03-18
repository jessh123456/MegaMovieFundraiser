"""This version checks to see if there is only ONE ticket left and, if so,
produces a more appropriately worded statement"""


# Initialize loop so that it runs at least once
name = ""
count = 0
MAX_TICKETS = 5

while name != "Xxx" and count != 5:
    if MAX_TICKETS - count > 1:
        print(f"\nYou have {MAX_TICKETS - count} seats left")
    else:
        print(f"\nYou only have ONE seat left!")
    # Get details
    name = input("Whats your name? ").title()
    count += 1

if count < MAX_TICKETS:
    print(f"\nYou have sold {count} tickets\nThere are still "
          f"{MAX_TICKETS - count} available")
else:
    print("\nYou have sold all the available tickets")
