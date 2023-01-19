print("Welcome to the Utopia, where you can relax and do whatever you want")

# Start Location
location = "The Woods"

while True:
    # Print the current location
    print("You are currently in the " + location)

    # Print available options
    if location == "The Woods":
        print("1. Go north")
        print("2. Go east")
        print("3. Go west")
        choice = input("What would you like to do? ")

        if choice == "1":
            location = "The mountains"
        elif choice == "2":
            location = "The river"
        elif choice == "3":
            location = "The village"
        else:
            print("Invalid choice, please try again.")

    elif location == "The mountains":
        print("1. Go south")
        print("2. Climb the mountain")
        choice = input("What would you like to do? ")

        if choice == "1":
            location = "The Woods"
        elif choice == "2":
            print("You have reached the summit of the mountain!")
        else:
            print("Invalid choice, please try again.")
    # etc for other location
    elif location == "The village":
        print("1. Talk to the shopkeeper")
        print("2. Go to the inn")
        print("3. Go back to the Woods")
        choice = input("What would you like to do? ")

        if choice == "1":
            print("The shopkeeper tells you about a treasure hidden in the mountain.")
        elif choice == "2":
            print("You rest for the night at the inn.")
        elif choice == "3":
            location = "The Woods"
        else:
            print("Invalid choice, please try again.")
    elif location == "The river":
        print("1. Go fishing")
        print("2. Go back to the forest")
        choice = input("What would you like to do? ")

        if choice == "1":
            print("You caught a fish!")
        elif choice == "2":
            location = "The Woods"
        else:
            print("Invalid choice, please try again.")
