# This program receives input form the user 
# and square numbers that are greater than 5

def check_if_int(ask_user):
    if type(ask_user) == 'class int':
        print("You entered an integer of {}".format(ask_user))
    else:
        print("Invalid input")


ask_user = input("Enter a number: \n")
