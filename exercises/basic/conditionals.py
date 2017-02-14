class MathBot:
	def solve(self, int1, int2, isMultiply):
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
		output += str(n2)+"\t= "
		output += str(self.solve(n1,n2,isMultiply))
		print(output)

mathBot = MathBot()
print("MathBot says:")
mathBot.printEquation(6,12, True)
mathBot.printEquation(100,1, False)
mathBot.printEquation(36,3, True)
mathBot.printEquation(12,9, True)
mathBot.printEquation(77,34, False)
mathBot.printEquation(11,22, False)
print("Which also means 'Hello!' MathBot just likes different equations")





