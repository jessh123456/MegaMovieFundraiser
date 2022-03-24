"""Includes testing loop.
This component, originally designed to ask if the user wants to purchase
snacks, asks for a Yes/No response and keeps asking - for the purposes of
testing. In this version the program makes a decision based on the first
letter of the response.
"""


def yes_no_response(question):
    error_message = "Please answer 'Y' or 'N'"
    valid_response = ["y", "yes", "n", "no"]
    response = input(question).lower()
    while response not in valid_response:
        print(error_message)
        response = input(question).lower()

    if response[0] == "n":
        return False
    else:
        return True


# Main routine
# Temporary input statements - during development
testing = True
while testing:
    snacks_required = yes_no_response("Do you want snacks?")
    if not snacks_required:
        print("Valid answer. You don't want snacks")
    else:
        print("Valid answer. You do want snacks")
    print()
