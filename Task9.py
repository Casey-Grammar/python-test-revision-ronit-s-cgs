# Task 9 Cat problem
# You've collected too many cats. Write a program to count how
# many cats you have by reading in their names. All your cats only
# have first names, with no spaces.

def main():
    #Write your code here
    catlist = input("Cats: ")
    catnames = catlist.split()
    print(f"You have " + str(len(catnames)) + ' cats')




    # End of your code here





if __name__ == '__main__':
    main()