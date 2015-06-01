class ChkAcct(object):
	"""Checking account class"""
	def __init__(self, ID="", funds=0):
		self.acct_ID = ID
		try:
			self.__Balance = int(funds)
		except:
			print "Invalid opening checking account balance requested, zero (0) used!"
			self.__Balance = 0
		print "Checking account numbered", self.acct_ID, "created"
		print "Opening checking account balance is: ", self.__Balance
		
	def __getBal(self):
		return self.__Balance
	def __setBal(self, funds=0):
		self.__Balance = int(funds)
	
	balance = property(__getBal, __setBal)
	
	def Deposit(self, funds=0):
		self.balance += int(funds)
	def Withdrawal(self, funds=0):
		self.balance -= int(funds)
	def Transfer(self, funds=0, savings=None):
		self.balance -= int(funds) 
		savings.Deposit(funds=funds)
		
class SavAcct(object):
	"""Savings account class"""
	def __init__(self, ID="", funds=0):
		self.acct_ID = ID
		try:
			self.__Balance = int(funds)
		except:
			print "Invalid opening checking account balance requested, zero (0) used!"
			self.__Balance = 0
		print "Savings account numbered", self.acct_ID, "created"
		print "Opening savings account balance is:", self.__Balance
		
	def __getBal(self):
		return self.__Balance
	def __setBal(self, funds=0):
		self.__Balance = int(funds)
	
	balance = property(__getBal, __setBal)
	
	def Deposit(self, funds=0):
		self.balance += int(funds)
	def Withdrawal(self, funds=0):
		self.balance -= int(funds)
	def Transfer(self, funds=0, checking=None):
		self.balance -= int(funds) 
		checking.Deposit(funds=funds)
