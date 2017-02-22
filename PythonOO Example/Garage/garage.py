class Garage():
	def __init__(self, vehicles):
		self.vehicles = vehicles
	
	def addVehicle(self, newVehicle):
		self.vehicles.append(newVehicle)
	
	def viewVehicles(self):
		for v in self.vehicles:
			print("ID:", v.id, ", Bill:", v.baseBill)
	
	def removeVehicle(self, ID):
		for v in self.vehicles:
			if v.id == ID:
				self.vehicles.remove(v)
	
	def removeAllVehicles(self):
		for x in range((len(self.vehicles)-1), -1, -1):
			print(x)
			del self.vehicles[x]
			
	def returnVehicleByWheelie():
		# not done on notes?
		print("TODO")