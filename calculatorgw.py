import sys

def verifyInput(prompt):

    while True:
    
        try:
            value = float(prompt) # Variable to check if the input is a number
            if value > 0: # Check if the input is greater than 0
                prompt = value
                return prompt
            else:
                print("\nInput must be greater than 0.")
                prompt = input("\nEnter the value: ")
                verifyInput(prompt) # Recursive call to verifyInput

        except ValueError: # In case the value doesn't return as a number, the user must type the correct input
            print("\nInput must be a number.")
            prompt = input("\nEnter the value: ")
            verifyInput(prompt) # Recursive call to verifyInput
     
def efficiencyDefense():

    defenseHour = input("\nCurrent lib%/h: ")
    defenseHour = verifyInput(defenseHour)
    # Current lib%/h on the planet

    defensePop = input("\nCurrent population: ")
    defensePop = verifyInput(defensePop)
    # Current population on the planet

    invasionLevel = input("\nInvasion level: ")
    invasionLevel = verifyInput(invasionLevel)
    # The invasion level on the planet

    efficiencyOnDefense = ((defenseHour * (invasionLevel / 20)) / (defensePop / 10000))

    print(f"\nEfficiency on Defense: {efficiencyOnDefense:.2f}")
    input("\nPress Enter to continue...")
    # Wait for user input to continue

def popNeededDefense():

    defenseHour = input("\nNeeded lib%/h: ")
    defenseHour = verifyInput(defenseHour)
    # Needed lib%/h on the planet

    defenseEff = input("\nCurrent efficiency: ")
    defenseEff = verifyInput(defenseEff)
    # Current efficiency on the planet

    invasionLevel = input("\nInvasion level: ")
    invasionLevel = verifyInput(invasionLevel)
    # The invasion level on the planet

    popNeededOnDefense = ((defenseHour * (invasionLevel / 20)) / (defenseEff / 10000))

    print(f"\nPop% needed on Defense: {popNeededOnDefense:.2f}")
    input("\nPress Enter to continue...")
    # Wait for user input to continue

def expectedLibDefense():

    defensePop = input("\nCurrent population: ")
    defensePop = verifyInput(defensePop)
    # Current population on the planet

    defenseEff = input("\nCurrent efficiency: ")
    defenseEff = verifyInput(defenseEff)
    # Current efficiency on the planet

    invasionLevel = input("\nInvasion level: ")
    invasionLevel = verifyInput(invasionLevel)
    # The invasion level on the planet

    expectedLibOnDefense = (defenseEff / 10000) / ((invasionLevel / 20) / defensePop)

    print(f"\nExpected Liberation%/h on Defense: {expectedLibOnDefense:.3f}")
    input("\nPress Enter to continue...")
    # Wait for user input to continue


def neededLibDefense():

    currentLibHour = input("\nCurrent lib%/h: ")
    currentLibHour = verifyInput(currentLibHour)
    # For ramp up time

    currentLibProgress = input("\nCurrent progress on the planet: ")
    currentLibProgress = verifyInput(currentLibProgress)
    # Current progress on the planet

    currentLibProgress += currentLibHour * 1.5
     # It gets the current liberation on the planet and adds the ramp up time

    timeLeft = input("\nTime left for the invasion (in hours): ")
    timeLeft = verifyInput(timeLeft)
    # Time left to defend the planet

    timeLeft -= 1.5 # Ramp up time until we reach max liberation

    neededLibPerHourDefense = (currentLibProgress / timeLeft)
    print(f"\nNeeded lib%/h to Defend in time: {neededLibPerHourDefense:.2f}")
    input("\nPress Enter to continue...")
    # Wait for user input to continue
    
def efficiencyLiberation():

    liberationHour = input("\nCurrent lib%/h: ")
    liberationHour = verifyInput(liberationHour)
    # Current lib%/h on the planet

    liberationPop = input("\nCurrent population: ")
    liberationPop = verifyInput(liberationPop)
    # Current population on the planet

    efficiencyOnLiberation = ((liberationHour / liberationPop) * 10000)

    print(f"\nEfficiency on Liberation: {efficiencyOnLiberation:.2f}")
    input("\nPress Enter to continue...")
    # Wait for user input to continue

def popNeededLiberation():
    
    liberationHour = input("\nCurrent lib%/h: ")
    liberationHour = verifyInput(liberationHour)
    # Current lib%/h on the planet

    liberationEff = input("\nCurrent efficiency: ")
    liberationEff = verifyInput(liberationEff)
    # Current efficiency on the planet

    popNeededOnLiberation = (liberationHour / (liberationEff / 10000))

    print(f"\nPop% needed on Liberation: {popNeededOnLiberation:.2f}")
    input("\nPress Enter to continue...")
    # Wait for user input to continue

def expectedLibLiberation():
    
    liberationPop = input("\nCurrent population: ")
    liberationPop = verifyInput(liberationPop)
    # Current population on the planet

    liberationEff = input("\nCurrent efficiency: ")
    liberationEff = verifyInput(liberationEff)
    # Current efficiency on the planet

    expectedLibOnLiberation = ((liberationEff / 10000) * liberationPop)

    print(f"\nExpected Liberation%/h on Liberation: {expectedLibOnLiberation:.3f}")
    input("\nPress Enter to continue...")
    # Wait for user input to continue

def neededLibLiberation():

    currentLibHour = input("\nCurrent lib%/h: ")
    currentLibHour = verifyInput(currentLibHour)
    # For ramp up time

    currentLibProgress = input("\nCurrent progress on the planet: ")
    currentLibProgress = verifyInput(currentLibProgress)
    # Current progress on the planet

    currentLibProgress += currentLibHour * 1.5
    # It gets the current liberation on the planet and adds the ramp up time

    timeLeft = input("\nTime left to liberate (in hours): ")
    timeLeft = verifyInput(timeLeft)
    # Time left to liberate the planet

    timeLeft -= 1.5 # Ramp up time until we reach max liberation

    planetDecay = input("\nPlanet decay in %: ")
    planetDecay = verifyInput(planetDecay)
    # Have to input the planet decay for liberation

    neededLibPerHourLiberation = (currentLibProgress / timeLeft) + planetDecay
    # Calculate the needed liberation per hour considering planet decay

    print(f"\nNeeded lib%/h to Liberate in time: {neededLibPerHourLiberation:.2f}")
    input("\nPress Enter to continue...")
    # Wait for user input to continue

def invasion():
    while True:
        print("\nGalactic War Calculator - Invasion")
        print("\nSelect what you want to know:\n")
        print("1 - Efficiency")
        print("2 - Population needed")
        print("3 - Expected liberation %/h")
        print("4 - Needed liberation %/h")
        print("0 - Return")

        opcao = input("\nEnter the option: ") 

        while opcao not in ['0', '1', '2', '3', '4']:
            print("\nInput must be valid.")
            opcao = input("\nEnter the option: ")
            # Keep the loop until a valid option is entered

        if opcao == '0':
            print("\nReturning to the main menu.")
            break # Returns to the main menu
    
        elif opcao == '1':
            print("\nEfficiency selected.")
            efficiencyDefense() # Call function for efficiency

        elif opcao == '2':
            print("\nPopulation needed selected.")
            popNeededDefense() # Call function for population needed

        elif opcao == '3':
            print("\nExpected liberation %/h selected.")
            expectedLibDefense() # Call function for expected liberation %/h

        elif opcao == '4':
            print("\nNeeded liberation %/h selected.")
            neededLibDefense() # Call function for needed liberation %/h

def liberation():

    while True:
        print("\nGalactic War Calculator - Liberation")
        print("\nSelect what you want to know:\n")
        print("1 - Efficiency")
        print("2 - Population needed")
        print("3 - Expected liberation %/h")
        print("4 - Needed liberation %/h")
        print("0 - Return")

        option = input("\nEnter the option: ") 

        while option not in ['0', '1', '2', '3', '4']:
            print("\nInput must be valid.")
            option = input("\nEnter the option: ")
            # Keep the loop until a valid option is entered

        if option == '0':
            print("\nReturning to the main menu.")
            break # Returns to the main menu
    
        elif option == '1':
            print("\nEfficiency selected.")
            efficiencyLiberation() # Call function for efficiency

        elif option == '2':
            print("\nPopulation needed selected.")
            popNeededLiberation() # Call function for population needed

        elif option == '3':
            print("\nExpected liberation %/h selected.")
            expectedLibLiberation() # Call function for expected liberation %/h

        elif option == '4':
            print("\nNeeded liberation %/h selected.")
            neededLibLiberation() # Call function for needed liberation %/h

def main():
    while True:
        print("Galactic War Calculator")
        print("Select the type of Campaign:\n")
        print("1 - Defense/Invasion")
        print("2 - Liberation")
        print("0 - Exit\n")

        option = input("Enter the option: ")

        while option not in ['0', '1', '2']:
            print("\nInput must be valid.")
            option = input("\nEnter the option: ")
        # Keep the loop until a valid option is entered

        if option == '0':
            print("\nExiting the calculator.")
            sys.exit()
            # Exit the program
        elif option == '1':
            print("\nDefense/Invasion selected.")
            # Call the function for Defense
            invasion()
        elif option == '2':
            print("\nLiberation selected.")
            # Call the function for Liberation
            liberation()

if __name__ == "__main__":
    main()