# Task 4 Open Sesame
# Write a program to ask Ali for a password. 
# If the password is correct, the cave door will be opened. 
# Otherwise nothing will

attpassword = input("What is the password, Ali?:")

def main():
    if attpassword == "Open Sesame!":
      print("Correct, the door has opened")
    else: 
      print("Wrong, try again.")






if __name__ == '__main__':
    main()