from abc import ABC, abstractmethod

class Vehicle(ABC):
	def __init__(self, id, colour, baseBill):
		self.id = id
		self.colour = colour
		self.baseBill = baseBill
	
	#must be overridden to before class can be instantiated
	@abstractmethod
	def beep(self):
		pass
		#old way of doing it
		#raise NotImplementedError ("subclass must implement beep method")
	
	def turnOnEngine(self):
		#code to do this
		pass