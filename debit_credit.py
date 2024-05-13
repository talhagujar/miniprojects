class Account:
    def __init__(self, acc_bal, acc_no) -> None:
        self.acc_bal = acc_bal
        self.acc_no = acc_no

        #For debit amount
    def debit(self, amount):
        self.acc_bal -= amount
        print("Rs.", amount , "was debited")
        print("Total bal is.", self.get_bal())

        #For credit amount
        
    def credit(self, amount):
        self.acc_bal += amount
        print("Rs.", amount , "was credited")
        print("Total bal is.", self.get_bal())


        
    def get_bal(self):
       return self.acc_bal

while True:
    c1 = Account(11000, 11110014442)
    uc = int(input("""
 1. for debit
 2. for credit
 3. exit
"""))
     
    if uc == 1:
       nmbr = int(input("Please enter amount"))
       c1.debit(nmbr)

    elif uc == 2:    
       cnmbr = int(input("Please enter amount"))
       c1.credit(cnmbr)
    else:
        break
 


