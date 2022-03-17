"""Added 01_name_not_blank_v3 to original v1 of this base code"""

# Import statements

# Functions go here

# Check that ticket name is not blank
def not_blank(question):
    while True:
        response = input(question)
        if not response.isalpha():
            print("You can't leave this blank...")
        else:
            return response


# ******* Main routine *******

# Set up dictionaries / lists to hold data

# Ask user if they have used the program before and
# show instructions if necessary

# Loop to get ticket details

    # Get name (can't be blank)
    name = not_blank("What's your name: ")

    # Get age (between 12-130)

    # Calculate ticket price

    # Loop to ask for snacks

    # calculate snack price

    # Ask for payment method (And apply surcharge if necessary)

# Calculate total sales and profit

# Output data to text file
