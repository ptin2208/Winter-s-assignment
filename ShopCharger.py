from StudentCard import StudentCard
import datetime
class ShopCharger:
    __insertedStudentCard = None

    @staticmethod
    #get inserted card
    def insertStudentCard(studentID):
        ShopCharger.__insertedStudentCard = StudentCard.getStudentCard(studentID)
  
    @staticmethod
    def chargeMoney(money):
        #card is inserted
        if not ShopCharger.__insertedStudentCard is None:
            temp = ShopCharger.__insertedStudentCard.getBalance() + money
            #balance is enough
            if temp >= 0:
                ShopCharger.__insertedStudentCard.setBalance(ShopCharger.__insertedStudentCard.getBalance() + money)
                ShopCharger.printBalance()
                
                now = datetime.datetime.now()
                history = now.strftime("%Y-%m-%d %H:%M")
                if money < 0:
                    history += " Withdraw - Amount: " + str(-money)
                else:
                    history += " Deposit - Amount: " + str(money)
                
                ShopCharger.__insertedStudentCard.writeHistory(history)
                return
            #balance is not enough
            else:
                return
        #card is not inserted
        else: 
            print('学生証が挿入されていません')
            return
    @staticmethod
    def printBalance():
        print("残高を表示します");
        print("学生名:" + ShopCharger.__insertedStudentCard.getStudentName());
        print("残高:" + str(ShopCharger.__insertedStudentCard.getBalance()));
        return
    
    @staticmethod
    def printHistory():
        return ShopCharger.__insertedStudentCard.getHistory()
            
        