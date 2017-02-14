import random

class MathBotV3:
	def solve(self, int1, int2, isMultiply):
		if int1==0 or int2==0:
				return max(int1,int2)
		
		if isMultiply:
			return int1 * int2
		else:
			return int1 + int2

	def printLoop(self, n1, iterations):
		iterations -= 1
		isMultiply = random.choice([True, False])
		n2 = random.randint(0,10)
		result = self.solve(n1,n2,isMultiply)
		output = ""
		output += str(n1)+" "
		if isMultiply:
			output +="* "
		else:
			output +="+ "
		output += str(n2)+" = "
		output += str(result)
		output += ", "
		if iterations>0:
			output += self.printLoop(result, iterations)
		return output

mathBot = MathBotV3()
print("Danger Will Robinson! A rogue MathBot is out of control!!\n")
print(mathBot.printLoop(1,50))
print("\nArgh! The equations are too much, save yourself!")






