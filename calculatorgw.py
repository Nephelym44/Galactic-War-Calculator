# Made by: Nephelym :D

import sys, subprocess

def verifyInput(prompt):

    while True:
    
        try:
            value = float(prompt) # Variable to check if the input is a number
            if value >= 0: # Check if the input is greater or equal to 0
                prompt = value
                return prompt
            else:
                print("\nInput must be greater than or equal to 0.")
                prompt = input("\nEnter the value: ")
                verifyInput(prompt) # Recursive call to verifyInput

        except ValueError: # In case the value doesn't return as a number, the user must type the correct input
            print("\nInput must be a number.")
            prompt = input("\nEnter the value: ")
            verifyInput(prompt) # Recursive call to verifyInput

##################################################################################################################################

def efficiency():

    print("\nConsult Helldivers Companion App for the current lib%/h.")
    liberationPerHour = input("\nCurrent lib%/h: ")
    liberationPerHour = verifyInput(liberationPerHour)
    # Current lib%/h on the planet

    print("\nConsult Helldivers Companion App for the current population on the planet.")
    activePopulation = input("\nCurrent population in %: ")
    activePopulation = verifyInput(activePopulation)

    if activePopulation == 0:
        print("\nPopulation must be greater than 0.")
        activePopulation = input("\nCurrent population in %: ")
        activePopulation = verifyInput(activePopulation)
        
    # Current population on the planet

    print("\nConsult Helldivers Companion App for the total HP of the planet.")
    planetLevel = input("\nTotal HP in Level (each level is 50k HP): ")
    planetLevel = verifyInput(planetLevel)
    # The invasion level on the planet

    efficiency = ((liberationPerHour * (planetLevel / 20)) / (activePopulation / 10000))

    print(f"\nEfficiency on planet: {efficiency:.2f}\n")
    input("\nPress Enter to continue...")
    # Wait for user input to continue

    subprocess.run("cls", shell=True) # Clear the console

def popNeeded():

    print("\nConsult Helldivers Companion App for the current lib%/h.")
    currentLibHour = input("\nCurrent lib%/h: ")
    currentLibHour = verifyInput(currentLibHour)
    # For ramp up time

    print("\nConsult Helldivers Companion App for current decay on the planet (for Liberation Campaign).")
    planetDecay = input("\nPlanet decay (in %): ")
    planetDecay = verifyInput(planetDecay)

    print("\nConsult Helldivers Companion App for the current progress on the planet.")
    planetProgress = input("\nCurrent progress on the planet in %: ")
    planetProgress = verifyInput(planetProgress)
    # Current progress on the planet 

    print("\nConsult Helldivers Companion App for the time left.")
    timeLeft = input("\nTime left for the campaign (in hours): ")
    timeLeft = verifyInput(timeLeft)
    # Time left to defend the planet

    rampUpTime = input("\nRamp up time (in hours): ")
    rampUpTime = verifyInput(rampUpTime)
    # Time for liberation to stabilize

    neededLiberationPerHour = neededLiberation(currentLibHour, planetDecay, planetProgress, timeLeft, rampUpTime)

    if neededLiberationPerHour == 0:
        print("\nPlanet will be liberated before the ramp up time ends.")
        input("\nPress Enter to continue...")
        subprocess.run("cls", shell=True)
        return

    print("\nConsult Helldivers Companion App for the total HP of the planet.")
    planetLevel = input("\nTotal HP in Level (each level is 50k HP): ")
    planetLevel = verifyInput(planetLevel)
    # The invasion level on the planet

    efficiency = input("\nAverage efficiency (use efficiency function): ")
    efficiency = verifyInput(efficiency)
    # Average efficiency

    popNeeded = ((neededLiberationPerHour * (planetLevel / 20)) / (efficiency / 10000))

    print(f"\nPop% needed on the planet: {popNeeded:.2f}%\n")
    input("\nPress Enter to continue...")
    # Wait for user input to continue

    subprocess.run("cls", shell=True) # Clear the console

def popNeededWithRegions():

    print("\nConsult Helldivers Companion App for the current lib%/h.")
    currentLibHour = input("\nCurrent lib%/h: ")
    currentLibHour = verifyInput(currentLibHour)
    # For ramp up time

    print("\nConsult Helldivers Companion App for current decay on the planet (for Liberation Campaign).")
    planetDecay = input("\nPlanet decay (in %): ")
    planetDecay = verifyInput(planetDecay)

    print("\nConsult Helldivers Companion App for the current progress on the planet.")
    planetProgress = input("\nCurrent progress on the planet in %: ")
    planetProgress = verifyInput(planetProgress)
    # Current progress on the planet 

    print("\nConsult Helldivers Companion App for the time left.")
    timeLeft = input("\nTime left for the campaign (in hours): ")
    timeLeft = verifyInput(timeLeft)
    # Time left to defend the planet

    rampUpTime = input("\nRamp up time (in hours): ")
    rampUpTime = verifyInput(rampUpTime)
    # Time for liberation to stabilize

    neededLiberationPerHour = neededLiberation(currentLibHour, planetDecay, planetProgress, timeLeft, rampUpTime)

    if neededLiberationPerHour == 0:
        print("\nPlanet will be liberated before the ramp up time ends.")
        input("\nPress Enter to continue...")
        subprocess.run("cls", shell=True)
        return

    print("\nConsult Helldivers Companion App for the total HP of the planet.")
    planetLevel = input("\nTotal HP in Level (each level is 50k HP): ")
    planetLevel = verifyInput(planetLevel)
    # Planet total HP in level form

    efficiency = input("\nAverage efficiency (use efficiency function): ")
    efficiency = verifyInput(efficiency)
    # Average efficiency

    if efficiency == 0:
        print("\nEfficiency must be greater than 0.")
        efficiency = input("\nAverage efficiency: ")
        efficiency = verifyInput(efficiency)

    planetHP = planetLevel * 50000
    planetHP = planetHP - ((planetProgress / 100) * planetHP)

    nSet, nTow, nCit, nMega, nRegions = 0, 0, 0, 0, 0 # To start each variable at 0
    SettlementHP = 100000
    TownHP = 200000
    CityHP = 400000
    MegaCityHP = 600000
    # Each city type HP
    citiesListOrder = [] # To start the list of cities in order

    subprocess.run("cls", shell=True) # Clear the console

    while True:

        print("Select the type of cities present in the planet")
        print("In case a region has already been taken, don't add it.")
        print("Please select the regions in order from first available to last available.")
        print("Consult Helldivers Companion App for this information.")
        print("Repeat this until done.")
        print(f"\nNumber of each city: Settlement ({nSet}), Town ({nTow}), City ({nCit}), Mega City ({nMega})")
        print("\n1 - Settlements (100k HP)")
        print("\n2 - Towns (200k HP)")
        print("\n3 - Cities (400k HP)")
        print("\n4 - Mega Cities (600k HP)")
        print("\n0 - Continue\n")
        option = input("\nSelect the option: ")
        
        while option not in ['0', '1', '2', '3', '4']:
            print("\nInput must be valid.")
            option = input("\nSelect the option: ")
            # Keep the loop until a valid option is entered

        if option == '0':
            break
            # Break the loop to continue to the next step

        elif option == '1':
            nSet += 1
            nRegions += 1
            citiesListOrder.append("Settlement")
            subprocess.run("cls", shell=True)

        elif option == '2':
            nTow += 1
            nRegions += 1
            citiesListOrder.append("Town")
            subprocess.run("cls", shell=True)

        elif option == '3':
            nCit += 1
            nRegions += 1
            citiesListOrder.append("City")
            subprocess.run("cls", shell=True)

        elif option == '4':
            nMega += 1
            nRegions += 1
            citiesListOrder.append("Mega City")
            subprocess.run("cls", shell=True)

    i, j = 0, 0 # Counter for the number of regions

    # Settlement: 3.9h aproximadamente, assumindo 35% da população nas cidades
    # Town: 6.07h aproximadamente, assumindo 35% da população nas cidades
    # City: 11.65h aproximadamente, assumindo 35% da população nas cidades
    # Mega City: 17.23h aproximadamente, assumindo 35% da população nas cidades
    # NÃO CONTANDO COM DECAY!!!!!
    # Assumindo 35% da população e 1025 de efficiency

    while i <= nRegions:

        if i == 0: # Calculation for when no regions liberated
            planetHPLevel = int(round(planetHP / 50000))
            popNeededOnRegions = ((neededLiberationPerHour * (planetHPLevel / 20)) / (efficiency / 10000))
            print(f"\nPop% needed on the planet with ({i}) regions: {popNeededOnRegions:.2f}%\n")
            i += 1

        elif nSet > 0 and citiesListOrder[j] == 'Settlement': 

            planetHP = planetHP - (SettlementHP * 0.5)
            planetHPLevel = int(round(planetHP / 50000))

            if citiesListOrder[j] == []:
                print("\nLista vazia")
                break

            popNeededOnRegions = ((neededLiberationPerHour * (planetHPLevel / 20)) / (efficiency / 10000))
            print(f"\nPop% needed on the planet with ({i}) regions: {popNeededOnRegions:.2f}%\n")
            print("Region type: Settlement")

            nSet -= 1
            i += 1
            j += 1

        elif nTow > 0 and citiesListOrder[j] == 'Town': 

            planetHP = planetHP - (TownHP * 1.5)
            planetHPLevel = int(round(planetHP / 50000))
            popNeededOnRegions = ((neededLiberationPerHour * (planetHPLevel / 20)) / (efficiency / 10000))
            print(f"\nPop% needed on the planet with ({i}) regions: {popNeededOnRegions:.2f}%\n")
            print("Region type: Town")

            nTow -= 1
            i += 1
            j += 1

        elif nCit > 0 and citiesListOrder[j] == 'City': 

            planetHP = planetHP - (CityHP * 1.5)
            planetHPLevel = int(round(planetHP / 50000))
            popNeededOnRegions = ((neededLiberationPerHour * (planetHPLevel / 20)) / (efficiency / 10000))
            print(f"\nPop% needed on the planet with ({i}) regions: {popNeededOnRegions:.2f}%\n")
            print("Region type: City")

            nCit -= 1
            i += 1
            j += 1

        elif nMega > 0 and citiesListOrder[j] == 'Mega City': 

            planetHP = planetHP - (MegaCityHP * 1.5)
            planetHPLevel = int(round(planetHP / 50000))
            popNeededOnRegions = ((neededLiberationPerHour * (planetHPLevel / 20)) / (efficiency / 10000))
            print(f"\nPop% needed on the planet with ({i}) regions: {popNeededOnRegions:.2f}%\n")
            print("Region type: Mega City")

            nMega -= 1
            i += 1
            j += 1

        # WORK IN PROGRESS!!!!!!!!!!!
        # Pop% needed doesn't work as intended, show numbers way below the expected and negative numbers in certain cases
        # Fix: Try calculating pop% needed using the total HP of the planet - region bonus like Marshall said.
        # Example: Get the total HP of the planet, then subtract the HP of the regions bonus and calculate the pop% needed with that HP for each case.


    input("\nPress Enter to continue...")
    subprocess.run("cls", shell=True) # Clear the console

def expectedLiberation():

    print("\nConsult Helldivers Companion App for the current population on the planet.")
    activePopulation = input("\nCurrent population: ")
    activePopulation = verifyInput(activePopulation)
    # Current population on the planet

    print("\nUse the efficiency function to get this number.")
    efficiency = input("\nAverage efficiency: ")
    efficiency = verifyInput(efficiency)
    # Current efficiency on the planet

    print("\nConsult Helldivers Companion App for the total HP of the planet.")
    planetLevel = input("\nTotal HP in Level (each level is 50k HP): ")
    planetLevel = verifyInput(planetLevel)
    # The invasion level on the planet

    expectedLiberation = (efficiency / 10000) / ((planetLevel / 20) / activePopulation)

    print(f"\nExpected Liberation%/h on the planet: {expectedLiberation:.3f}%\n")
    input("\nPress Enter to continue...")
    # Wait for user input to continue

    subprocess.run("cls", shell=True) # Clear the console


def neededLiberation(currentLibHour, planetDecay, currentProgress, timeLeft, rampUpTime):

    currentProgress = currentProgress + (currentLibHour * rampUpTime)
    # It gets the current liberation on the planet and adds the ramp up time
    currentProgress = 100 - currentProgress
    # It gets the needed liberation progress to reach 100%

    if currentProgress < 0:
        print("\nPlanet will be liberated before the ramp up time ends.")
        return 0
        
    timeLeft -= rampUpTime

    neededLiberationPerHour = (currentProgress / timeLeft) + planetDecay
    return neededLiberationPerHour  

def callneededLiberation():
    print("\nConsult Helldivers Companion App for the current lib%/h.")
    currentLibHour = input("\nCurrent lib%/h: ")
    currentLibHour = verifyInput(currentLibHour)
    # For ramp up time

    print("\nConsult Helldivers Companion App for current decay on the planet (for Liberation Campaign).")
    planetDecay = input("\nPlanet decay (in %): ")
    planetDecay = verifyInput(planetDecay)

    print("\nConsult Helldivers Companion App for the current progress on the planet.")
    planetProgress = input("\nCurrent progress on the planet in %: ")
    planetProgress = verifyInput(planetProgress)
    # Current progress on the planet in decimal

    print("\nConsult Helldivers Companion App for the time left.")
    timeLeft = input("\nTime left for the campaign (in hours): ")
    timeLeft = verifyInput(timeLeft)
    # Time left to defend the planet

    rampUpTime = input("\nRamp up time (in hours): ")
    rampUpTime = verifyInput(rampUpTime)
    # Time for liberation to stabilize

    neededLiberationPerHour = neededLiberation(currentLibHour, planetDecay, planetProgress, timeLeft, rampUpTime)

    print(f"\nNeeded Liberation%/h on the planet: {neededLiberationPerHour:.3f}%\n")
    input("\nPress Enter to continue...")
    # Wait for user input to continue

    subprocess.run("cls", shell=True) # Clear the console

def etaLiberatePlanet():

    print("\nConsult Helldivers Companion App for the current lib%/h.")
    currentLibHour = input("\nLiberation per hour: ")
    currentLibHour = verifyInput(currentLibHour)
    # For ramp up time

    print("\nConsult Helldivers Companion App for current decay on the planet (for Liberation Campaign).")
    planetDecay = input("\nPlanet decay (in %): ")
    planetDecay = verifyInput(planetDecay)

    print("\nConsult Helldivers Companion App for the current progress on the planet.")
    planetProgress = input("\nCurrent progress on the planet in %: ")
    planetProgress = verifyInput(planetProgress)

    currentLibHour -= planetDecay

    etaLiberatePlanet = (100 - planetProgress) / currentLibHour
    # Calculates the expected time to liberate the planet

    hours = int(etaLiberatePlanet)
    minutes = int((etaLiberatePlanet - hours) * 60)

    print(f"\nExpected time to liberate the planet: {hours}h{minutes}min\n")
    input("\nPress Enter to continue...")
    # Wait for user input to continue

    subprocess.run("cls", shell=True) # Clear the console

def popNeededReachLib():

    print("")
    liberationHour = input("\nLiberation %/h required: ")
    liberationHour = verifyInput(liberationHour)

    print("\nUse the efficiency function to get this number.")
    efficiency = input("\nAverage efficiency: ")
    efficiency = verifyInput(efficiency)
    # Current efficiency on the planet

    print("\nConsult Helldivers Companion App for the total HP of the planet.")
    planetLevel = input("\nTotal HP in Level (each level is 50k HP): ")
    planetLevel = verifyInput(planetLevel)
    # The invasion level on the planet

    popNeeded = ((liberationHour * (planetLevel / 20)) / (efficiency / 10000))

    print(f"\nPop% needed on the planet to reach expected liberation: {popNeeded:.2f}%\n")
    input("\nPress Enter to continue...")
    # Wait for user input to continue

    subprocess.run("cls", shell=True) # Clear the console




##################################################################################################################################

def invasion():
    
    subprocess.run("cls", shell=True) # Clear the console

    while True:
        print("\nGalactic War Calculator - Invasion")
        print("\nSelect what you want to know:\n")
        print("1 - Efficiency")
        print("2 - Population needed without regions")
        print("3 - Population needed with regions (Work in Progress)")
        print("4 - Population needed to reach a specific liberation %/h")
        print("5 - Expected liberation %/h")
        print("6 - Needed liberation %/h")
        print("7 - Expected time to liberate planet")
        print("0 - Return")

        opcao = input("\nEnter the option: ") 

        while opcao not in ['0', '1', '2', '3', '4', '5', '6', '7']:
            print("\nInput must be valid.")
            opcao = input("\nEnter the option: ")
            # Keep the loop until a valid option is entered

        if opcao == '0':
            subprocess.run("cls", shell=True) # Clear the console
            break # Returns to the main menu
    
        elif opcao == '1':
            print("\nEfficiency selected.")
            efficiency() # Call function for efficiency

        elif opcao == '2':
            print("\nPopulation needed without regions selected.")
            popNeeded() # Call function for population needed

        elif opcao == '3':
            print("\nWork in Progress!!!!!!!!!!")
            #popNeededWithRegions() # Call function for population needed with regions

        elif opcao == '4':
            print("\nPopulation needed to reach a specific liberation %/h selected.")
            popNeededReachLib() # Call function for population needed

        elif opcao == '5':
            print("\nExpected liberation %/h selected.")
            expectedLiberation() # Call function for expected liberation %/h

        elif opcao == '6':
            print("\nNeeded liberation %/h selected.")
            callneededLiberation()

        elif opcao == '7':
            print("\nExpected time to liberate planet selected.")
            etaLiberatePlanet()


##################################################################################################################################

def liberation():

    subprocess.run("cls", shell=True) # Clear the console

    while True:
        print("\nGalactic War Calculator - Liberation")
        print("\nSelect what you want to know:\n")
        print("1 - Efficiency")
        print("2 - Population needed without regions")
        print("3 - Population needed with regions (Work in Progress)")
        print("4 - Population needed to reach a specific liberation %/h")
        print("5 - Expected liberation %/h")
        print("6 - Needed liberation %/h")
        print("7 - Expected time to liberate planet")
        print("0 - Return")

        opcao = input("\nEnter the option: ") 

        while opcao not in ['0', '1', '2', '3', '4', '5', '6', '7']:
            print("\nInput must be valid.")
            opcao = input("\nEnter the option: ")
            # Keep the loop until a valid option is entered

        if opcao == '0':
            subprocess.run("cls", shell=True) # Clear the console
            break # Returns to the main menu
    
        elif opcao == '1':
            print("\nEfficiency selected.")
            efficiency() # Call function for efficiency

        elif opcao == '2':
            print("\nPopulation needed without regions selected.")
            popNeeded() # Call function for population needed

        elif opcao == '3':
            print("\nWork in Progress!!!!!!!!!!")
            #popNeededWithRegions() # Call function for population needed with regions

        elif opcao == '4':
            print("\nPopulation needed to reach a specific liberation %/h selected.")
            popNeededReachLib() # Call function for population needed

        elif opcao == '5':
            print("\nExpected liberation %/h selected.")
            expectedLiberation() # Call function for expected liberation %/h

        elif opcao == '6':
            print("\nNeeded liberation %/h selected.")
            callneededLiberation()

        elif opcao == '7':
            print("\nExpected time to liberate planet selected.")
            etaLiberatePlanet()


##################################################################################################################################

def hodEffectivePopulation():
    subprocess.run("cls", shell=True) # Clear the console

    print("Galactic War Calculator - HOD Effective Population\n")
    currentPopulation = input("Insert the current population on the planet: ")
    currentPopulation = verifyInput(currentPopulation) 
    # Gets the current population on the planet and verify the input

    currentEffectivePopulation = ((currentPopulation * 3) / (100 + currentPopulation * 2)) * 100
    # Calculates the effective population with HOD active

    print(f"\nEffective Population with HOD active: {currentEffectivePopulation:.2f}%\n")
    input("\nPress Enter to continue...")
    # Wait for user input to continue

    subprocess.run("cls", shell=True) # Clear the console

##################################################################################################################################

def main():

    while True:
        print("Galactic War Calculator")
        print("Select the sub-menu:\n")
        print("1 - Invasion")
        print("2 - Liberation")
        print("3 - HOD Effective Population")
        print("0 - Exit\n")

        option = input("Enter the option: ")

        while option not in ['0', '1', '2', '3']:
            print("\nInput must be valid.")
            option = input("\nEnter the option: ")
        # Keep the loop until a valid option is entered

        if option == '0':
            print("\nExiting the calculator.\n")
            sys.exit()
            # Exit the program
        elif option == '1':
            # Call the function for Defense
            invasion()
        elif option == '2':
            # Call the function for Liberation
            liberation()
        elif option == '3':
            # Call the function for HOD Calculation
            hodEffectivePopulation()

if __name__ == "__main__":
    main()