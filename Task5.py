# Task 5 FIFA World Cup
# With 9 FIFA World Cup wins between them, Brazil and Italy two of
# the most successful soccer countries in the world. Write a program
# that works out who won their latest soccer match, given the scores
# of both teams.

itascore = int(input("Italy: "))
brascore = int(input("Brazil: "))
def main():
    if itascore > brascore:
        print("Italy won the match")
    elif brascore > itascore:
        print("Brazil won the match")
    elif brascore == itascore:
        print("The match was drawn")
   


    # End of your code here





if __name__ == '__main__':
    main()