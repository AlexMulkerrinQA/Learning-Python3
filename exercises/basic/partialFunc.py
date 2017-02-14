import random
from functools import partial

class MathBotV7:
	numberArray = []
	
	def solve(self, int1, int2, isMultiply, isPower):
		if int1==0 or int2==0:
				return max(int1,int2)
		
		if isMultiply:
			return int1 * int2
		elif isPower:
			result = 1
			for i in range(int2):
				result *= int1
			return result
		else:
			return int1 + int2
			
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

mathBot = MathBotV7()
numIn = mathBot.getInput("Please give an integer: ")
double = partial(mathBot.solve, int2=2, isMultiply=False, isPower=True)
triple = partial(mathBot.solve, int2=3, isMultiply=False, isPower=True)
print(str(numIn)+" doubled = "+str(double(numIn)))
print(str(numIn)+" tripled = "+str(triple(numIn)))

