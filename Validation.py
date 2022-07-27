def account_number_validation(accountNumber):
    
    if accountNumber:

        if len(str(accountNumber)) == 10:

            try:
                int(accountNumber)
                return True
            except ValueError:
                print("Invalid Account Number, Account Number Should be integer")
                return False  
            except TypeError:
                print('Invalid Account Type')
                return False  

        else:
            print("Account Number Cannot be more or less than 10 Digit")
            return False

    else:
        print("Account Number Is Required Field")
        return False

#def registration_input_validation(input):
    # check if it's a list
    # check each items in the list and be sure they are the correct data types 