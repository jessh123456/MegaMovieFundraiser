"""Noticed that the count is actually incorrect. In the previous version
the program was counting the XXX as a sold seat.
Also - further improved the emphasis - drawing the users attention when
there is only one seat left"""


# Initialize loop so that it runs at least once
name = ""
count = 0
MAX_TICKETS = 5

while name != "Xxx" and count != 5:
    if MAX_TICKETS - count > 1:
        print(f"\nYou have {MAX_TICKETS - count} seats left")
    else:
        # Warns user there is only one seat left
        print(f"\n***** You only have ONE seat left! *****")
    # Get details
    name = input("Whats your name? ").title()
    if name != "Xxx":
        count += 1

if count < MAX_TICKETS:
    print(f"\nYou have sold {count} tickets\nThere are still "
          f"{MAX_TICKETS - count} available")
else:
    print("\nYou have sold all the available tickets")
