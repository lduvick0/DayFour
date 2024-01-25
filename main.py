nameList= ["Jimmy", "James", "Lisa", "Augustine", "Orion"]
homeList=["Charlotte", "San Francisco", "Seattle", "Raleigh", "Orlando"]
foodList=["Cheeseburger", "Pizza", "Tacos", "Sushi", "Curry"]
contInput="y"
print("Welcome to the Academy Student Database")
print("Our current students are: "+ str(nameList))
firstchoice=input("Are you looking for a specific student (y/n) ")
if firstchoice=="n":
    print("{:20} {:20} {:20} ".format("Name","Hometown","Favorite Food"))
    print("{:<20} {:<20} {:<20}".format("=============", "=============", "============="))
    for i in range(0,len(nameList)):
        print("{:<20} {:<20} {:<20} ".format(nameList[i],homeList[i],foodList[i]))
    contInput="n"
while contInput=="y":
    numStudent=int(input("Which student number would you like to know about?: (0-4) "))
    if numStudent < 0 or numStudent > len(nameList)-1:
        print("Invalid input")
        goodNum = "n"
        while goodNum == "n":
            numStudent=int(input("Which student number would you like to know about? (0-4) "))
            if numStudent >= 0 or numStudent <=len(nameList)-1:
                goodNum = "y"
            else:
                print("Invalid number")

    print(nameList[numStudent])
    validCat="n"
    while validCat == "n":
        catChosen=input("What category would you like to see? (Hometown or Favorite Food) ")
        if catChosen.lower()=="hometown" or catChosen.lower()=="home" or catChosen.lower()=="town":
            print(homeList[numStudent])
            validCat="y"
        elif catChosen.lower()=="favorite food" or catChosen.lower()=="food" or catChosen.lower()=="favorite":
            print(foodList[numStudent])
            validCat="y"
        else:
            print("Sorry, I didn't understand please try again")

    contInput=input("Would you like to learn about another student? (y/n) ")
