# This program receives input form the user 
# and square numbers that are greater than 5

from tabnanny import verbose


def check_if_int(ask_user):
    joining_verified = ask_user
    if joining_verified <= 0 or joining_verified > 0:
        print("You entered an integer of {}".format(joining_verified))
        return joining_verified    
    else:
        return joining_verified
   
counter = 3
if counter > 0:
    try:
        ask_user = input("Enter a number: ")
        verify_user_input = check_if_int(ask_user)
        if verify_user_input == ask_user:
            double_number = (ask_user * ask_user)
            print("Double of {} is: {}.".format(ask_user,double_number))
    except  (NameError,SyntaxError) as ne:
        print("Invalid input")
    counter-1
    if counter <= 0:
        print("start again, programm closed")
        