# Task 8 Call signs
# A portmanteau is a word made by combining parts of two other
# words. This could be used to create call signs for an online
# group.

#For example, david and jones would make daones.

#Let's make some call signs!

#Write a program that asks a user for their first name and last
#name and then takes the first two letters of the first name and
#the last four letters of the last name and combines them to make
#a new call sign. (N.B. we won't test your program with any input
#that's too short!)

def main():
    #Write your code here
    name = input("First and Last Name? ")
    firstname = name.split()[0]
    lastname = name.split()[1]
    callsign = firstname[:2] + firstname[:-4]
    print(f"The new call sign is: {callsign} ")


    # End of your code here





if __name__ == '__main__':
    main()