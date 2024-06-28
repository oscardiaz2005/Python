from loginclass import*

def verify(user1,user2):
    if user1.getuser()==user2.getuser() and user1.getpassword()==user2.getpassword():
        return True
    else :
        return False