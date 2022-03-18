"""Added 02_Ticket_loop_v4"""

# Import statements

# Functions go here

# Check that ticket name is not blank
def not_blank(question):
    while True:
        response = input(question).title()
        if not response.isalpha():  # Ensures inout contains at least 1 letter
            print("You can't leave this blank...")  # Error if not
        else:
            return response  # Otherwise, return the input


# ******* Main routine *******

# Set up dictionaries / lists to hold data

# Ask user if they have used the program before and
# show instructions if necessary

# Loop to get ticket details
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
    name = input("Whats your name? ")   
    if name != "Xxx":
        count += 1  # Don't want to include escape code in the count

if count < MAX_TICKETS:
    print(f"\nYou have sold {count} tickets\nThere are still "
          f"{MAX_TICKETS - count} available")
else:
    print("\nYou have sold all the available tickets")

    # Get name (can't be blank)
    name = not_blank("What's your name: ")

    # Get age (between 12-130)

    # Calculate ticket price

    # Loop to ask for snacks

    # calculate snack price

    # Ask for payment method (And apply surcharge if necessary)

# Calculate total sales and profit

# Output data to text file
