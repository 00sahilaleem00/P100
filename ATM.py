class ATM(object):
    def __init__(self, cardNumber, PIN, balance):
        self.cardNumber = cardNumber
        self.PIN = PIN
        self.balance = balance

    def cashWithdrawal(self, amount):
        userPIN = input("Enter PIN: ")
        if userPIN == self.PIN:
            self.balance -= int(amount)
            print("Withdrawing amount "+str(amount) +
                  " from card "+self.cardNumber)
        else:
            print("Wrong PIN!!!")

    def cashDeposit(self, amount):
        userPIN = input("Enter PIN: ")
        if userPIN == self.PIN:
            self.balance += int(amount)
            print("Depositing amount "+str(amount) +
                  " into card "+self.cardNumber)

    def balanceEnquiry(self):
        userPIN = input("Enter PIN: ")
        if userPIN == self.PIN:
            print("Your current balance is "+str(self.balance))
        else:
            print("Wrong PIN!!!")


card1 = ATM("123456", "1921", 100000)
card2 = ATM("943514", "6845", 100)

card1.cashWithdrawal(100)
card1.balanceEnquiry()
card1.cashDeposit(100)
card1.balanceEnquiry()

card2.cashWithdrawal(1000)
card2.balanceEnquiry()
card2.cashDeposit(-100)
card2.balanceEnquiry()
