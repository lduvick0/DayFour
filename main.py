nameList= ["Jimmy", "James", "Lisa", "Augustine", "Orion"]
homeList=["Charlotte", "San Francisco", "Seattle", "Raleigh"]
foodList=["Cheeseburger", "Pizza", "Tacos", "Sushi", "Curry"]
contInput="y"
while contInput=="y":
    numStudent=int(input("Which student number would you like to know about?: (0-4)"))
    if numStudent < 0 or numStudent > len(nameList)-1:
        print("Invalid input")
        goodNum = "n"
        while goodNum == "n":
            numStudent=int(input("Which student number would you like to know about? (0-4)"))
            if numStudent >= 0 or numStudent <=len(nameList)-1:
                goodNum = "y"
            else:
                print("Invalid number")

    print(nameList[numStudent])
    catChosen=input("What category would you like to see? (Hometown or Favorite Food)")
    if catChosen.lower()=="hometown":
        print(homeList[numStudent])
    elif catChosen.lower()=="favorite":
        print(foodList[numStudent])
    else:
        print("Sorry, I didn't understand please try again")
    contInput=input("Would you like to learn about another student? (y/n")
