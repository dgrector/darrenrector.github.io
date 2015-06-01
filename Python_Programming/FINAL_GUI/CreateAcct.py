from Tkinter import *
bg="#009999"
fg="dark blue"

blnProcess = False

#### event procedures ####
def Reset():
    entChkItems.delete(0,END)
    entSavItems.delete(0,END)
    entChkStItems.delete(0,END)
    entSavStItems.delete(0,END)
    entChkItems.focus()
    

def Process():
    strChkItems=entChkItems.get()
    strSavItems=entSavItems.get()
    strChkStItems=entChkStItems.get()
    strSavStItems=entSavStItems.get()
##    return value
    if  len(strChkItems) >0 or len(strSavItems)>0:
        blnProcess=True
        lblData["text"] = "Account Successfully Created!"
    else:
        Reset()
        lblData["text"]= "Account Unsuccessfully Created!"
        entChkItems.focus()
def Continue():
    myForm.destroy()
    
        


###########################       
myForm = Tk()
myForm["bg"] = bg
myForm.title("Create Account")
myForm.geometry("800x500")
lblLogo1=Label(text="Choose which account to open", bg=bg, fg=fg, font="Arial 14 bold")
lblLogo1.place(x=255, y=20)
lblChecking = Label(text="Checking", fg=fg, bg=bg, font="Arial 12 bold")
lblChecking.place(x=270, y=115)
lblSavings = Label(text="Savings", fg=fg, bg=bg, font="Arial 12 bold")
lblSavings.place(x=615, y=115)
######Account # Label######
lblChkItems = Label (text="Enter Checking Account #", fg=fg, bg=bg, font="Arial 12 bold")
lblChkItems.place(x=50, y=150)
entChkItems = Entry(bg="light grey", fg="black", font="Arial 12", width=10)
entChkItems.place(x=270, y=150)
lblSavItems = Label (text="Enter Savings Account #", fg=fg, bg=bg, font="Arial 12 bold")
lblSavItems.place(x=400, y=150)
entSavItems = Entry(bg="light grey", fg="black", font="Arial 12", width=10)
entSavItems.place(x=615, y=150)
######Starting Balance Label######
lblChkStItems = Label (text="Enter a starting balance", fg=fg, bg=bg, font="Arial 12 bold")
lblChkStItems.place(x=50, y=200)

entChkStItems = Entry(bg="light grey", fg="black", font="Arial 12", width=10)
entChkStItems.place(x=270, y=200)

lblSavStItems = Label (text="Enter a starting balance", fg=fg, bg=bg, font="Arial 12 bold")
lblSavStItems.place(x=400, y=200)

entSavStItems = Entry(bg="light grey", fg="black", font="Arial 12", width=10)
entSavStItems.place(x=615, y=200)

lblData = Label (fg="red", bg=bg, font="Arial 14 bold")                                          #successful label color
lblData.place(x=375, y=250)


######Action Buttons######

btnProcess = Button(text="Process", fg="dark blue", bg=bg, font="Arial 12 bold", width=10, command=Process)
btnProcess.place(x=408, y=425)

btnReset = Button(text="Reset", fg="dark blue", bg=bg, font="Arial 12 bold", width=10, command=Reset)
btnReset.place(x=525, y=425)
    
btnClose = Button(text="Continue", fg="dark blue", bg=bg, font="Arial 12 bold", width=10, command=Continue)
btnClose.place(x=642, y=425)

entChkItems.focus()
myForm.mainloop()




