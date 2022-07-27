# CRUD

def create(accountNumber,userDetails):

    completion_state = False

    try:

        f = open("data/User_record/" + str(accountNumber) + ".txt", "x")
    
    except UnboundLocalError:

        print("User Already Exist")

        return completion_state

    else:

        f.write(str(userDetails));
        completion_state = True

    finally:

        create(f)
        return completion_state

def Create(f):
    f.close();
    


    

    
 
 # create a file
 # name of the file will be accountNumber.txt
 # add the user details to the file
 # return true
 # if saving to file fails, then delete created file

def read(userAccountNumber):
    print("read user record")


def update(userAccountNUmber):
    print("update user record")


def delete(userAccountnumber):
    print("delete user record")    


def find(userAccountNumber):
    print("find user record")
