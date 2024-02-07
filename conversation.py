Year=2023

print("Welcome !!")
name = input("Whats your name: ")
print("\nHello,",name,"!")
birthYear = int (input("What year were you born? "))
# this formula subtracts the current year and your birth year to find your age
age = Year - birthYear
print("Nice to meet you,",name)
print("\nYour birth year is",birthYear,"and you are",age,"years old")
team=input("\nWhats your favorite football team? ( full team name like cowboys or buccaneers)")
# this if statement is a funny way of showing what my favorite team is to the user
if team != "buccaneers":
    print("\nI feel sorry for you liking that team.")
    print("My favorite is the buccaneers !")
else:
    print("\nThat's my favorite team too!")
favNumber= int(input("\nWhat's your favorite number? "))
# this easy formula doubles the user input for favNumber
doubleFav= favNumber * 2
print("\nyour favorite number is:", favNumber, "and if you double that number it is:", doubleFav)
print("\nIts been nice talking too you, here is a summary of all the information from our conversation")
print("\nYour name is", name, "you are", age, "years old and your favorite football team is the", team)
print("Finally your favorite number is", favNumber)