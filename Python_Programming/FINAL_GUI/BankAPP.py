from Tkinter import *           #import Tkinter
from ChkSav import *            #import 
from BankGUI import *
from CreateAcct import *

objChkAcct = ChkAcct()          #creates checking object
objSavAcct = SavAcct()          #creates savings object

myForm = Tk()                   #creates empty form
myForm.title("Bank")            #sets window title
myForm.geometry("800x500")      #sets base window size
myForm["bg"] = "#009999"        #sets background color

"""Objects"""
objGUI = BankGUI(master=myForm, ChkAcct=objChkAcct, SavAcct=objSavAcct)

myForm.mainloop()               #makes window/frame visible

