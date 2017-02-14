import random, time

class MathBotV6:
	numberArray = []
	
	def solve(self, int1, int2, isMultiply):
		if int1==0 or int2==0:
				return max(int1,int2)
		
		if isMultiply:
			return int1 * int2
		else:
			return int1 + int2
	
	def setnumberArray(self, length):
		self.numberArray = []
		for i in range(length):
			self.numberArray.append(random.randint(0,10))
		
	def loopMultiply(self,multiplier):
		index=0
		for i in self.numberArray:
			self.numberArray[index] = self.solve(i,multiplier,True)
			index+=1
			
	def getInput(self, prompt):
		number = -1
		while number<0:
			userIn = input(prompt)
			try:
				number = int(userIn)
			except ValueError:
				print("Error: "+userIn+" is not a valid number",)
			else:
				if number<0:
					print("Error: number must be positive",userIn)
		#print(str(number) + " is a valid number",)
		return number

mathBot = MathBotV6()
numIn = mathBot.getInput("Please give array size: ")
mathBot.setnumberArray(numIn)
print(mathBot.numberArray)
multIn = mathBot.getInput("Please give multiplier: ")
mathBot.loopMultiply(multIn)
print(mathBot.numberArray)


