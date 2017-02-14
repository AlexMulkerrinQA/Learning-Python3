class MathBotV2:
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
		output += str(n2)+"\t= "
		output += str(self.solve(n1,n2,isMultiply))
		print(output)

mathBot = MathBotV2()
print("Warning: MathBot V2 Premium-Pro-Xtra-Adv-Edition(TM) has erronorous behaviour!")
mathBot.printEquation(2,2,False)
mathBot.printEquation(1,0,True)
print("Error! Error! Non-zero result given when zero expected --- SYSTEM OVER ---")






