"""3rd iteration of the integer checking function
Simplified try/except and created AGE_RANGE as a constant
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
AGE_RANGE = range(12, 111)  # between 12 and 110 inclusive
age = number_checker("Please enter the age of the ticket-holder: ")
while age not in AGE_RANGE:  # age must be between 12 and 110
    age = number_checker("\nPlease enter an integer between 12 and 110: ")
print(f"Age = {age}")
