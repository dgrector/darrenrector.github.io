from Tkinter import *
class BankGUI(object):
    """Bank GUI"""
    ######Default colors/fonts######
    bg="#009999"
    fg="dark blue"
    f1="Arial 16 bold"
    f2="Arial 14 bold"
    f3="Arial 14"
    ################################
    def __init__(self, master=None, ChkAcct=None, SavAcct=None):
        self.master = master
        self.ChkAcct = ChkAcct
        self.SavAcct = SavAcct
        self.controlsOnForm()
        self.entItems.focus()

    def controlsOnForm(self):
        self.lblBankName = Label(text="DGR ACCOUNTS", fg=self.fg, bg=self.bg, font=self.f1)
        self.lblBankName.place(x=325, y=10)
        self.lblItems = Label(text="Funds:", fg=self.fg, bg=self.bg, font=self.f2)
        self.lblItems.place(x=300, y=60)
        self.entItems = Entry(bg="white", fg="black", font=self.f2, width=10)
        self.entItems.place(x=375, y=60)
        self.lblChecking = Label(text="Checking", fg=self.fg, bg=self.bg, font=self.f2)
        self.lblChecking.place(x=205, y=125)
        self.lblSavings = Label(text="Savings", fg=self.fg, bg=self.bg, font=self.f2)
        self.lblSavings.place(x=530, y=125)
    ######Checking Buttons######
        self.btnWithdrawal = Button(text="Withdrawal", bg=self.bg, fg="dark blue", font=self.f3, width=12,command=self.CWithdrawal)
        self.btnWithdrawal.place(x=180, y=175)
        self.btnDeposit = Button(text="Deposit", bg=self.bg, fg="dark blue", font=self.f3, width=12,command=self.CDeposit)
        self.btnDeposit.place(x=180, y=225)
        self.btnTransfer = Button(text="Transfer", bg=self.bg, fg="dark blue", font=self.f3, width=12,command=self.CTransfer)
        self.btnTransfer.place(x=180, y=275)
    ######Savings Buttons######
        self.btnWithdrawal = Button(text="Withdrawal", bg=self.bg, fg="dark blue", font=self.f3, width=12,command=self.SWithdrawal)
        self.btnWithdrawal.place(x=500, y=175)
        self.btnDeposit = Button(text="Deposit", bg=self.bg, fg="dark blue", font=self.f3, width=12,command=self.SDeposit)
        self.btnDeposit.place(x=500, y=225)
        self.btnTransfer = Button(text="Transfer", bg=self.bg, fg="dark blue", font=self.f3, width=12,command=self.STransfer)
        self.btnTransfer.place(x=500, y=275)
    ######Balance######
        self.lblChkBal = Label (text="Balance:", fg=self.fg, bg=self.bg, font=self.f2)
        self.lblChkBal.place(x=160, y=350)
        self.lblChkBalAmt = Label (text="0", fg=self.fg, bg=self.bg, font=self.f2)
        self.lblChkBalAmt.place(x=285, y=350)
        
        self.lblSavBal = Label (text="Balance:", fg=self.fg, bg=self.bg, font=self.f2)
        self.lblSavBal.place(x=480, y=350)
        self.lblSavBalAmt = Label (text="0", fg=self.fg, bg=self.bg, font=self.f2)
        self.lblSavBalAmt.place(x=605, y=350)
    ######Action Buttons######
        self.btnReset = Button(text="Reset", fg="dark blue", bg=self.bg, font=self.f3, width=10, command=self.Reset)
        self.btnReset.place(x=500, y=425)
    
        self.btnClose = Button(text="Close", fg="red", bg=self.bg, font=self.f3, width=10, command=self.Close)
        self.btnClose.place(x=642, y=425)
    #####Set Focus######
        

    ######Event Procedures######

    ######Checking Events######
    def CWithdrawal(self):
        strFunds = self.entItems.get()
        self.ChkAcct.Withdrawal(funds=strFunds)
        self.lblChkBalAmt["text"] = self.ChkAcct.balance

    def CDeposit(self):
        strFunds = self.entItems.get()
        self.ChkAcct.Deposit(funds=strFunds)
        self.lblChkBalAmt["text"] = self.ChkAcct.balance

    def CTransfer(self):
        strFunds = self.entItems.get()
        self.ChkAcct.Transfer(funds=strFunds, savings=self.SavAcct)
        self.lblChkBalAmt["text"] = self.ChkAcct.balance
        self.lblSavBalAmt["text"] = self.SavAcct.balance

    ######Savings Events######
    def SWithdrawal(self):
        strFunds = self.entItems.get()
        self.SavAcct.Withdrawal(funds=strFunds)
        self.lblSavBalAmt["text"] = self.SavAcct.balance

    def SDeposit(self):
        strFunds = self.entItems.get()
        self.SavAcct.Deposit(funds=strFunds)
        self.lblSavBalAmt["text"] = self.SavAcct.balance

    def STransfer(self):
        strFunds = self.entItems.get()
        self.SavAcct.Transfer(funds=strFunds, checking=self.ChkAcct)
        self.lblSavBalAmt["text"] = self.SavAcct.balance
        self.lblChkBalAmt["text"] = self.ChkAcct.balance

    ######Action Events######
    def Reset(self):
        self.entItems.delete(0,END)

    def Close(self):
        self.master.destroy()
