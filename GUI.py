import tkinter
from StudentCard import StudentCard

class GUI(tkinter.Tk):  
    def __init__(self):
        tkinter.Tk.__init__(self)
        
        self.__inputID = ""
        #add label and input field
        self.inputLabel = tkinter.Label(self, text = "Input Student's ID Number:")
        self.inputLabel.grid(row = 0, column = 0)
        self.errorLabel = tkinter.Label(self, text = "Invalid Student's ID number", fg = "red")
        self.inputField = tkinter.Entry(self)
        self.inputField.grid(row = 1, column = 0)
        
        #add buttons
        #enter button
        self.enterButton = tkinter.Button(self, text = "Enter", command = self.getID)
        self.enterButton.grid(row = 4, column = 1)
        #close button
        self.closeButton = tkinter.Button(self, text = "Close", command = self.destroy)
        self.closeButton.grid(row = 4, column = 3)

    
    def getID(self):
        self.__inputID = self.inputField.get()
        #if studentID is found, destroy Tk
        if StudentCard.getStudentCard(self.__inputID) != None:
            self.destroy()    
        #if not found, display error message
        else: 
            self.errorLabel.grid(row = 3, column = 0)
            
    def getInputCard(self):
        return StudentCard.getStudentCard(self.__inputID)