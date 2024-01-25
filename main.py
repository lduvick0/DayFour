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
    validCat="n"
    while validCat == "n":
        catChosen=input("What category would you like to see? (Hometown or Favorite Food)")
        if catChosen.lower()=="hometown" | catChosen.lower()=="home" | catChosen.lower()=="town":
            print(homeList[numStudent])
            validCat="y"
        elif catChosen.lower()=="favorite food" or catChosen.lower()=="food" or catChosen.lower()=="favorite":
            print(foodList[numStudent])
            validCat="y"
        else:
            print("Sorry, I didn't understand please try again")

    contInput=input("Would you like to learn about another student? (y/n)")
