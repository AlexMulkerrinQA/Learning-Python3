import vehicle

class Motorbike(vehicle.Vehicle):
	def __init__(self, id, colour, baseBill, canWheelie):
		super().__init__(id, colour, baseBill)
		self.canWheelie =canWheelie
		
	def doWheelie(self):
		if (canWheelie):
			print("You did a sick wheelie")
		else:
			print("Your bike sucks")
	
	def beep(self):
		print("boop")