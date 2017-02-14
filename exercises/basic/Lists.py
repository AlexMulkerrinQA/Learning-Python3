import random

class MathBotV4:
	numberRation = []
	
	def setNumberRation(self,rationIn):
		self.numberRation = rationIn
		print("MathBot: *om-nom-nom*")

	def solve(self, int1, int2, isMultiply):
		if int1==0 or int2==0:
				return max(int1,int2)
		
		if isMultiply:
			return int1 * int2
		else:
			return int1 + int2

	def printEquation(self, n1, n2, isMultiply):
		output = ""
		output += str(n1)+" "
		if isMultiply:
			output +="* "
		else:
			output +="+ "
		output += str(n2)+" = "
		output += str(self.solve(n1,n2,isMultiply))
		print(output)
		
	def eatRation(self):
		n2 = 0
		for i in self.numberRation:
			isMultiply = random.choice([True, False])
			result = self.solve(i,n2,isMultiply)
			self.printEquation(i,n2,isMultiply)
			n2 = result
		self.numberRation = []
		print("MathBot is still hungry ;_;")

mathBot = MathBotV4()
print("The scourge of out-of-control MathBots has been halted by severely curtailing their acces to numbers. Yes I know, it is harsh but necessary...\n")
mathBot.setNumberRation([1,2,3,4,5,6,7,8,9,10])
mathBot.eatRation()







