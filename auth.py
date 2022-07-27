#from operator import ge
import random
import Database
import Validation
#from unicodedata import name


def init():
    
   
    print("Welcome to Quick Bank")

    haveAccount = int(input("Do you have An Account with us: 1 (Yes) 2 (No) \n"))

    if(haveAccount == 1):
        
        login()
    elif(haveAccount == 2):
        
        register()
    else:
        print("You have selected invalid option")
        init()


def login():
    
    print("++++ YOU'RE WELCOME TO OUR SPACE ++++")

    print("****** KINDLY LOGIN! ******")
    

    accountNumberFromUser = input("Write your Account Number? \n")

    isValidAccountNumaber = Validation.account_number_validation(accountNumberFromUser)

    if isValidAccountNumaber:

         password = input("Write your Password \n")

         for accountNumber,userDetails in Database.items():
             if(accountNumber == int(accountNumberFromUser)):
                 if(userDetails[3] == password):
                    bankOperation(userDetails) 

         print('Invalid account or Password')
         login()
    else:
        init()

                    
def register():

    print("******* Register ******")

    first_name = input("What is your First Name? \n")
    last_name = input("What is your Last Name? \n")
    email = input("What is your email address? \n")
    password = input("Create a Password? \n")

    accountNumber = generateAccountNumber()

    isUserCreated = Database.create(accountNumber, [first_name,last_name,email,password, 0])

    if isUserCreated:

        print("Your Account Has Been Created")
        print("== ==== ====== ===== ===")
        print("Your account number is: %d" % accountNumber)
        print("**** PLEASE KEEP IT SAVE!!! ****")
        print("== ==== ====== ===== ===")

        login()

    else:
        print("Something Went Wrong, Please Try Again")
        register()

def bankOperation(user):

    print("Welcome %s %s" % ( user[0], user[1] ) ) 

    selectedOption = input("what would you like to do? (1) deposit (2) withdrawal (3) logout (4) exit \n")


    if(selectedOption == 1):
        
        depositOperation()
    elif(selectedOption == 2):
        
        withdrawalOperation()
    elif(selectedOption == 3):
        
        logout()
    elif(selectedOption == 4):
        
        exit()
    else:
      
        print("Invalid option selected")
        bankOperation(user)
        

def withdrawalOperation():
    print("withdrawal")


def depositOperation():
    print("Deposit Operations")


def generateAccountNumber():
    return random.randrange(1111111111,9999999999)


def set_account_balance(userDetails, balance):
    userDetails[4] = balance


def get_current_balance(userDetails):
    return userDetails [4]


def logout():
    login()
  

init()