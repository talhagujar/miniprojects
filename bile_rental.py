class BikeRental:
    def __init__(self, stock) -> None:
        self.stock = stock

    def displaybike(self):
        print("Total bike", self.stock)
    def rentforbike(self, q):
        if q<=0:
            print("please enter positive value")
        elif q>self.stock:
            print("out of stock")
            
        else:
            print("Total price", q*100)
            print("Total bike's...", self.stock-q)
 
 
while True:
    obj = BikeRental(100)
    uc = int(input("""
1 Display bike
2 Rent bike
3 Exit
"""))
    if uc == 1:
        obj.displaybike ()
    elif uc == 2:
       n = int(input("Enter quantity..."))
       obj.rentforbike(n)
    else:
        break
