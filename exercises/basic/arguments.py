class SumBot:
	def summer(self,int1, int2):
		return int1 + int2

	def printSum(self, n1, n2):
		print(str(n1)+" + "+str(n2)+"\t= "+str(self.summer(n1,n2)))

summer = SumBot()
print("SumBot says:")
summer.printSum(20,52)
summer.printSum(100,1)
summer.printSum(43,65)
summer.printSum(80,28)
summer.printSum(77,34)
summer.printSum(11,22)
print("Which means 'Hello!' in BotMath :P")


