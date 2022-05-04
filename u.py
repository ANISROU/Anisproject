
def login():
    email=input("enter your email")

    if (email.endswith("@gmail.com")):
        password=input("enter your pass")
        if(len(password)<8):
            print("weak")
        else:
            print("succsus")
    elif(email.endswith("@yahoo.com")):
        print("error")
    else:
        print("error")
login()


