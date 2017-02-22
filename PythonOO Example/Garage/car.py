import vehicle

class Car(vehicle.Vehicle):
	def __init__(self, id, colour, baseBill, numWheels):
		super().__init__(id, colour, baseBill)
		self.numWheels = numWheels
	
	def beep(self):
		print("beep beep!")