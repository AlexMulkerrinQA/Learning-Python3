import random

class MathBotV5:
	numberRation = []
	
	def setNumberRation(self,rationIn):
		self.numberRation = rationIn
		print("MathBot: *om-nom-nom*")

	def printNumberRation(self,index):
		if index==0:
			print("MathBot: Oh please no, I have very few numbers Sir...")
			print("a "+str(self.numberRation[index])+",")
		elif index == len(self.numberRation)-1:
			print("and a "+str(self.numberRation[index])+".\n:((\n")
		else:
			print("a "+str(self.numberRation[index])+",")
		index+=1
		if index<len(self.numberRation):
			self.printNumberRation(index)

mathBot = MathBotV5()
mathBot.setNumberRation([1,2,3,4,5,6,7,8,9,10])
print("Hey you! Yes, you clanker, you! How many numbers did you just pilfer now? Answer me!")
mathBot.printNumberRation(0)
print("*Humph* You better not be one of those rational number junkies. Keep to what's natural, tincan.\n")
print("We'll be watching you....scum.")





