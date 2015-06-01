#Darren Rector
#5/12/2015
#Final_Project.py
#CCIS 1505


"""THIS PROGRAM DEMONSTARTES ACCEPTING USER INPUT, VALIDATING USER INPUT, CLASS/OBJECT CREATION, LOOPING
    CALCULATIONS, FILE I/O, EXCEPTION HANDLING, USING LISTS, USING FUNCTIONS AND DECISION MAKING"""

def GetNames():                                                                      #input data
    """This function will ask for the employee's first and last names"""
    strName = raw_input ("Enter the first and last name of the employee or press ENTER when finished.")
    return strName
    

def GetHours():                                                                       #data passed in and returned - process
    """This function asks for hours worked for a week and also
    checks if the user's input hour is between 1 and 60 hours"""
    blnDone = False
    while blnDone == False:                                                          #boolean loop off
        strEmpHours = raw_input("Enter the hours worked for this week, entries must be between 1 hour and 60 hours:")
        if len(strEmpHours) >0:
            intEmpHours = int(strEmpHours)
            if intEmpHours < 1 or intEmpHours > 60:                                   #Check the condition for employee's weekly hours input
                print "Please re-enter! Hours can not be less than 1 or more than 60!"
                blnDone=False
            else:
                blnDone = True                                                        #boolean loop on
        else:
            blnDone=True
    return intEmpHours
	
def GetRate():
    """"This function ask for an hourly rate of pay and also checks if the rate
        is between $6 and $20"""
    blnDone = False
    while blnDone == False:                                                           #boolean loop off
        strRate = raw_input("Enter the employee's hourly rate:")
        fltRate=float(strRate)
        if fltRate < 6 or fltRate > 20:                                               #Check the condition for employee hourly rate
             print "Please re-enter! hourly Rate Pay minimum $6 and maximum $20!"
             blnDone=False
        else:
            blnDone = True                                                            #boolean loop on
    return fltRate


######CREATING AVERAGE, HIGH AND LOW - MATHMATICAL CALCULATIONS######
"""Sort lowest pay in list"""
def Low(pay=[]):
    pay.sort()
    lowest = pay[0]
    return lowest
"""Sort highest pay in list"""
def High(pay=[]):
    pay.sort()
    highest = pay[len(pay) -1]
    return highest
"""Sort average pay"""
def Avg(pay =[]):
    intTotal = 0
    for pays in pay:
        intTotal += int(pays)#float
    avg =intTotal /len(pay)
    return avg
	
######CREATING EMPLOYEE CLASS######

class Employee(object):
    """This is for employee pay calculations"""

    def __init__(self, name = "", emphours = 0, rate = 0.0):        # constructor method
        self.Name = name.title()                                    # create public attribute - employee name
        self.EmpHours = int(emphours)                               # create public attribute - # of hours worked
        self.__Rate = float(rate)                                   # create private attribute - wage per hour
        print
        print "Employee's name is:", self.Name
        print "Number of hours worked:", self.EmpHours
        print "Employee's hourly wage is:", self.__Rate
        print

    def EmpPay(self):                                               # method to calculate the employee's weekly pay
        if self.EmpHours > 40:
            OTRate = 1.5 * self.__Rate
            OT = (self.EmpHours - 40)
            x=(40 * self.__Rate) + (OT * OTRate)
        else:
            x= self.EmpHours * self.__Rate
        return x
		
############MAINLINE############

lstEmpPay =[]                                                       #Store employee pay after calculating the hour * the payrate
blnDone = False
while blnDone == False:
    strName = GetNames()
    if len(strName)==0:                
        blnDone=True
        continue
    intHour = GetHours()
    fltRate = GetRate()
    if len(strName)>0:                                               #measures length of characters to ensure true entry
        objEmployee = Employee(name = strName, emphours = intHour, rate = fltRate)
        fltNums = objEmployee.EmpPay()
        lstEmpPay.append(fltNums)           
        blnDone =False
    else:
        blnDone =True    
print
print "The employees pay list: ", lstEmpPay
print
import cPickle                                                       #Import to use complex data files

try:
    filNumber = open("PAY.dat","w")                                  # open file to write
    cPickle.dump(lstEmpPay, filNumber)
    filNumber.close()
except(IOError), errMsg:                                             #I/O - error handling 
    print "Error writing PAY.dat file"
    print errMsg
    quit()                                                           #close file


try:
    filNumber = open("PAY.dat", "r")                                 # open file to read
    lstEmpPay = cPickle.load(filNumber)
    filNumber.close()

except(IOError), errMsg:                                             #I/O - error handling
    print "Error reading PAY.dat file"
    print errMsg
    quit()                                                           #close file
print

lstEmpPay.sort()

try:
    filNumber =open("SORTEDPAY.dat", "w")                           # open file to write
    lstEmpPay= cPickle.dump(lstEmpPay, filNumber)
    filNumber.close()
except(IOError), errMsg:
    print "Error reading SORTEDPAY.dat"
    print errMsg
    quit()                                                           #close file

try:
    filNumber = open("SORTEDPAY.dat", "r")                           # open file to read
    lstEmpPay = cPickle.load(filNumber)
    filNumber.close()

except(IOError), errMsg:                                             #I/O - error handling
    print "Error reading SORTEDPAY.dat file"
    print errMsg
    quit()                                                           #close file
print

"""Sorted Pay List"""
print "Here is the sorted employee pay: ", lstEmpPay                  

######AVERAGE, HIGH AND LOW RESULTS#######
print
intLow = Low(pay = lstEmpPay)
print "The lowest pay is: ",intLow

intHigh = High(pay = lstEmpPay)
print "The highest pay is: ",intHigh

intAvg = Avg(pay = lstEmpPay)
print "The average pay is: ",intAvg
print
print
                            
