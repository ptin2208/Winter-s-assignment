import tkinter
from StudentCard import StudentCard
from ShopCharger import ShopCharger as SC
from GUI import GUI

class MainFrame(tkinter.Tk):
    def __init__(self, studentCard):
        tkinter.Tk.__init__(self)
        
        self.studentCard = studentCard
        
        #set window's size        
        self.geometry("400x150")
        #set unresizable
        self.resizable(False, False)
        
        #set grid layout
        rows = 0
        while rows < 9:
            self.rowconfigure(rows, weight = 1)
            self.columnconfigure(rows, weight = 1)
            rows += 1
        
        #ID number
        self.idTextLabel = tkinter.Label(self, text = "Student's ID Number:")
        self.idTextLabel.grid(sticky = "W", row = 0, column = 0)
        self.idLabel = tkinter.Label(self, text = studentCard.getStudentID())
        self.idLabel.grid(sticky="E", row = 0, column = 6)
        
        #Name
        self.nameTextLabel = tkinter.Label(self, text = "Student's Name:")
        self.nameTextLabel.grid(sticky="W", row = 1, column = 0)
        self.nameLabel = tkinter.Label(self, text = studentCard.getStudentName())
        self.nameLabel.grid(sticky="E", row = 1, column = 6)
        
        #Balance
        self.balanceTextLabel = tkinter.Label(self, text = "Balance:")
        self.balanceTextLabel.grid(sticky="W", row = 2, column = 0)
        self.balanceLabel = tkinter.Label(self, text = studentCard.getBalance())
        self.balanceLabel.grid(sticky="E", row = 2, column = 6)
        
        #Buttons
        self.depositButton = tkinter.Button(self, text = "Deposit", command = self.deposit, height = 1, width = 15)
        self.depositButton.grid(row = 4, column = 0)
        self.invalidDepo = tkinter.Label(self, text = "Invalid Amount")
        
        
        self.withdrawButton = tkinter.Button(self, text = "Withdraw", command = self.withdraw, height = 1, width = 15)
        self.withdrawButton.grid(row = 6, column = 0)
        self.invalidWith = tkinter.Label(self, text = "Invalid Amount")
        
        
        self.historyButton = tkinter.Button(self, text = "Transaction History", command = self.showHistory, height = 1, width = 15)
        self.historyButton.grid(row = 8, column = 0)
        
        self.historyLabel = tkinter.Label(self, text = "")
        
        self.closeHisButton = tkinter.Button(self, text = "Close", command = self.closeHis)
        
        #Amount input fields
        self.depoVar = tkinter.IntVar(self, value = 0)
        self.depoInput = tkinter.Entry(self, textvariable = str(self.depoVar), width = 22)
        self.depoInput.grid(row = 4, column = 5)
        
        self.withVar = tkinter.IntVar(self, value = 0)
        self.withInput = tkinter.Entry(self, textvariable = str(self.withVar), width = 22)
        self.withInput.grid(row = 6, column = 5)
                
    def deposit(self):
        inputAmount = self.depoVar.get()
        if inputAmount <= 0:
            #display error message
            self.invalidDepo.grid(row = 5, column = 5)
        else:
            SC.insertStudentCard(self.studentCard.getStudentID())
            SC.chargeMoney(inputAmount)
            #update balance's data
            self.balanceLabel.config(text = self.studentCard.getBalance())
            #hide error message
            self.invalidDepo.grid_forget()
          
    def withdraw(self):
        inputAmount = self.withVar.get()
        
        if inputAmount <= 0 or inputAmount > self.studentCard.getBalance():
            #display error message
            self.invalidWith.grid(row = 7, column = 5)
        else:
            SC.insertStudentCard(self.studentCard.getStudentID())
            SC.chargeMoney(-inputAmount)
            #update balance's data
            self.balanceLabel.config(text = self.studentCard.getBalance())
            #hide error message
            self.invalidWith.grid_forget()
        
    def showHistory(self):
        history = ""
        for his in SC.printHistory():
            history += his + "\n"
        #display history
        self.historyLabel.config(text = history)
        self.geometry("400x300")
        self.historyLabel.grid(row = 9)
        
        #add close history button
        self.closeHisButton.grid()
        
    def closeHis(self):
        self.historyLabel.grid_forget()
        self.closeHisButton.grid_forget()
        self.geometry("400x150")
            
    
    def main():
        studentCard1 = StudentCard("a1", 'tut')  #add card 1 to list
        studentCard2 = StudentCard("b2", 'tenpaku')  #add card 2 to list
        
        gui = GUI()
        gui.mainloop()
        studentCard = gui.getInputCard()
        
        if not studentCard is None:
            from MainFrame import MainFrame as MF
            mainFrame = MF(studentCard)
            mainFrame.mainloop()

    if __name__ == '__main__' :
        import sys
        main()

        
   