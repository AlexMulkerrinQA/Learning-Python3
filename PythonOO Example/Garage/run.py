import time, vehicle, car, motorbike, garage

startVehicleList = []
addMore = True
idCount = 0

while (addMore):
	type = input("What type of vehicle would you like to add? ").lower()
	if type != "car" and type != "motorbike":
		print("That is not a valid vehicle type, please enter another")
		continue
	colour = input("What colour is your vehicle? ")
	baseBill = input("How much are you spending on your vehicle today? ")
	numWheels = 0
	canWheelie = False
	
	if type == "car":
		unknownNumWheels = True
		while (unknownNumWheels):
			try:
				numWheels = int(input("How many wheels does you vehicle have? "))
				unknownNumWheels = False
			except (ValueError):
				print("This is not a vlid number of wheels, please try again")
				
		startVehicleList.append(car.Car(idCount, colour, baseBill, numWheels))
		idCount += 1
	
	if type == "motorbike":
		unknownWheelie = True
		while (unknownWheelie):
			askWheelie = input("Can your vehicle do a wheelie? ").lower()
			if askWheelie == "yes":
				canWheelie = True
				unknownWheelie = False
			elif askWheelie == "no":
				canWheelie = False
				unknownWheelie = False
			else:
				print("That is not a valid answer, please try again")
		startVehicleList.append(motorbike.Motorbike(idCount, colour, baseBill, canWheelie))
		idCount += 1
	
	goAgain = input("Would you like to add another vehicle? ").lower()
	if goAgain == "no":
		addMore = False

myGarage = garage.Garage(startVehicleList)
active = True

choice = {'viewAll':1, 'add':2, 'remove':3, 'viewWheelie':4, 'beepAll':5, 'quit':10}
while (active):
	print("Welcome to your garage!")
	print("What would you like to do today?")
	print("1  - View all vehicles")
	print("2  - Add a new vehicle")
	print("3  - Remove a vehicle")
	print("4  - View a vehicle based on if it can wheelie")
	print("5  - Make all vehicles beep")
	print("10 - Quit")
	
	inp = input("")
	inp = int(inp)
	
	if inp == choice['viewAll']:
		myGarage.viewVehicles()
	elif inp == choice['add']:
		#add vehicle
		pass
	elif inp == choice['remove']:
		#remove vehicle
		pass
	elif inp == choice['viewWheelie']:
		myGarage.returnVehicleByWheelie()
	elif inp == choice['beepAll']:
		myGarage.makeVehiclesBeep()
	elif inp == choice['quit']:
		active = false
		break
	else:
		print ("That is not a valid option")
		time.sleep(2)