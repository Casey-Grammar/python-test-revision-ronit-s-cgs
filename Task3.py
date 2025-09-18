# Task 3: Dog Years
# Assume that a dog year is 7 human years. 
# Write a program that asks the user
def main():
    year = int(input("Dog years: "))
    hyear = year / 7
    print(f"Human years: {hyear}")

if __name__ == '__main__':
    main()