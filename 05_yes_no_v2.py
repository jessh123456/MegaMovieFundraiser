"""This function, keep asking if the user wants to purchase
snacks, asks for a Yes/No response and keeps asking for a valid response
is provided.
"""


def yes_no_response(question):
    error_message = "Please answer 'Y' or 'N'"
    valid_response = ["y", "yes", "n", "no"]
    response = input(question).lower()
    while response not in valid_response:
        print(error_message)
        response = input(question).lower()

    if response == "n" or response == "no":
        return False
    else:
        return True


# Main routine
# Temporary input statements - during development

snacks_required = yes_no_response("Do you want snacks?")
if not snacks_required:
    print("Valid answer. You don't want snacks")
else:
    print("Valid answer. You do want snacks")
