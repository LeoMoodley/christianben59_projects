import time

def scenario(description, options):
    print(description)
    time.sleep(2)

    response = input("\nWhat do you do?\n" + options).lower()

    while True:
        if response in ['a', 'b']:
            return response
        else:
            print("\nInvalid response. Please try again.")
            response = input().lower()

def introduction():
    response = scenario("It is 1:00 AM, and you are in your bed sound asleep.\nYou suddenly hear a bang coming from downstairs.", "Choose one of the following:\nA. Stay upstairs\nB. Go downstairs")

    if response == 'a':
        print("\nYou hear loud footsteps coming closer to your bedroom door.")
        scenario_2()
    elif response == 'b':
        print("\nYou sneak downstairs and do not find anything. It is quiet.")
        scenario_3()

def scenario_2():
    # Define the second scenario here
    pass

def scenario_3():
    # Define the third scenario here
    pass

# Start the game
introduction()

