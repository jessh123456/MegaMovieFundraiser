"""4th iteration of the integer checking function
Wanted to limit the possibility of getting a false age for children < 12
This meant creating upper and lower age limits as constants
"""


def number_checker(question):
    number = ""
    while not number:
        try:
            number = int(input(text))
            return number
        except ValueError:
            print("\nPlease enter an integer (i.e. a whole number with "
                  "no decimals)")


# ***** Main routine *****
# Check for a valid age
MAXIMUM_AGE = 110
MINIMUM_AGE = 12
age = number_checker("Please enter the age of the ticket-holder: ")
if age < MINIMUM_AGE:
    print("Sorry you are too young for this movie")
else:
    while age <= MAXIMUM_AGE:  # age must be between 12 and 110
        age = number_checker("\nPlease enter an integer between 12 and 110: ")
print(f"Age = {age}")
