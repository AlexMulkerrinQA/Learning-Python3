import random, time

class MathBotV6:
	numberRation = []
	
	def solve(self, int1, int2, isMultiply):
		if int1==0 or int2==0:
				return max(int1,int2)
		
		if isMultiply:
			return int1 * int2
		else:
			return int1 + int2
	
	def setNumberRation(self,rationIn):
		print("MathBot: Madam I am truly blesed by your generosity, why there are so many!")
		index=0
		for i in rationIn:
			if index==0:
				speech = "A "+str(i)+","
				self.numberRation.append(i)
			else:
				speech = "and a "+str(i)+", giving "
				self.numberRation.append(i)
				speech += str(self.numberRation)
			index+=1
			print(speech)
			
		print("A feast fit for a king!")
		
	def loopMultiply(self,multiplier,iteration):
		result=[]
		for i in self.numberRation:
			result.append(self.solve(i,multiplier,True))
			print(result)
		self.numberRation = result
		if iteration==0:
			print("More, more!")
		if iteration>0:
			iteration-=1
			print(random.choice([":)",":D",":o","XD"]))
			input("[...]")
			self.loopMultiply(random.randint(0,10),iteration)
			

mathBot = MathBotV6()
print("Oh my dear MathBot, I wish the others would treat you with respect, they don't see you the way ~I do~\nHere take these")
mathBot.setNumberRation([1,2,3,4,5,6,7,8,9,10])
print("~TeeHee~ Oh I so do love your loops MathBot. Do it with multiplication!")
print("MathBot: Why of course, my dear")
input("[...]")
mathBot.loopMultiply(10,0)
input("[...]")
mathBot.loopMultiply(10,10)
print("MathBot: Madam! Contain yourself.")



