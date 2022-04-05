"""Moved the check of sales against maximum tickets into its own function
Added lists to hold ticket holder's name and the price paid for their ticket
Added a dictionary to get data from these two new lists
Added code to append name and ticket price to the new lists (line 137 and 138)
Added the import re and import pandas libraries (installing pandas package if
necessary)
added the print statement for ticket profit on line 151
Modified the 'else' statements under 'if MAX_TICKETS - ticket_count > 1:'
(previously occupied lines 158-160) to improve flow and readability
Added the print details (movie_frame: bottom 3 lines) Which uses the pandas
library to create a printable Dataframe based on the dictionary
"""

# Import statements
import re
import pandas  # Might need to install pandas if library does not already exist


# Functions go here
# calculate ticket price (based on given5 age)
def calculate_ticket_price(age):
    # Ages - anything over standard_age must qualify for retired price
    child_age = range(12, 16)
    standard_age = range(16, 65)

    child_price = 7.5
    standard_price = 10.5
    retired_price = 6.5

    if age in child_age:
        price = child_price
    elif age in standard_age:
        price = standard_price
    else:
        price = retired_price

    return(price)
# Check that ticket name is not blank


def not_blank(question):
    while True:
        response = input(question).title()
        if not response.isalpha():  # Ensures inout contains at least 1 letter
            print("You can't leave this blank...")  # Error if not
        else:
            return response  # Otherwise, return the input


#  Check for valid integer (e.g. age)
def number_checker(question):
    number = ""
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print("\nPlease enter an integer (i.e. a whole number with "
                  "no decimals)")


def check_max_tickets(maximum, sold):
    if maximum - sold > 1:
        print(f"\nThere are {maximum - sold} tickets left")
    else:
        # warns the user that there is only one seat left
        print(f"\n***** There is only ONE ticket left! *****")


def check_valid_age(minimum, maximum):
    age = number_checker(f"Please enter {name}'s age")
    if age < minimum:
        print(f"Sorry, {name} is too young for this movie")
        return None
    else:
        while not age <= maximum:  # age must be between 12 and 110
            age = number_checker(f"\nAt {age} {name} is very old. "
                                 f"Please re-enter {name}'s age: ")
        return age
# ******* Main routine *******

# Set up dictionaries / lists to hold data
all_names = []
all_tickets = []


# Data frame dictionary
movie_data_dict = {
    "Name": all_names,
    "Tickets": all_tickets
}

MAXIMUM_AGE = 110
MINIMUM_AGE = 12
MAX_TICKETS = 5
TICKET_COST_PRICE = 5.00
name = ""
ticket_count = 0
profit = 0
# Ask user if they have used the program before and
# show instructions if necessary

# Loop to get ticket details
# Initialize loop so that it runs at least once

while name != "Xxx" and ticket_count != 5:
    # Check to ensure there are still tickets left
    check_max_tickets(MAX_TICKETS, ticket_count)
    # Get details
    # get name
    name = not_blank("Enter ticket-holder's name: ")
    if name == "Xxx":
        break
    else:
        # check for valid age and then calculate ticket price
        age = check_valid_age(MINIMUM_AGE, MAXIMUM_AGE)
        if not age:
            continue  # restarts the get ticket loop
        else:
            ticket_count += 1  # Don't want escape code in the ticket_count

        # Calculate ticket price
        ticket_price = calculate_ticket_price(age)
        print(f"For {name} the price is ${ticket_price:,.2f}")
        profit += (ticket_price - TICKET_COST_PRICE)

        # add name and ticket price to lists
        all_names.append(name)
        all_tickets.append(ticket_price)



# Calculate total sales and profit
if ticket_count < MAX_TICKETS:
    if ticket_count > 1:
        print(f"\n{ticket_count} tickets have now been sold")
    else:
        print("1 ticket has now been sold")
    if MAX_TICKETS - ticket_count > 1:
        print(f"{MAX_TICKETS - ticket_count} tickets are still available\n")
    else:
        print("1 ticket is still available\n")  # making sure it reads OK when
        # only one ticket left
else:
    print("\n!!!!!!!! All the available tickets have now been sold!!!!!!!!")
    print("*" * 60)

# Print details
movie_frame = pandas.DataFrame(movie_data_dict)
print(movie_frame)
print(f"\nProfit is {profit:,.2f}")

    # Get age (between 12-130)

    # Calculate ticket price

    # Loop to ask for snacks

    # calculate snack price

    # Ask for payment method (And apply surcharge if necessary)



# Output data to text file
