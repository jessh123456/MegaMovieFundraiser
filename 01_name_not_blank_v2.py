def not_blank(question, error_message):
    valid = ""
    while not valid:
        response = input(question)
        if not response:
            print(error_message)
        else:
            return response


# ****** Main routine ******
name = not_blank("What's your name: ", "You can't leave this blank...")
