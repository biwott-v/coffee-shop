from customer import Customer
from coffee import Coffee 

class Order(Customer,Coffee):
    all_coffee,temp_coffee=[],[]
    all_customers={}
    def __init__(self,price ):
        Customer.__init__(self,name)
        Coffee.__init__(self,coffee_name)
        self._price = price
        all_coffee.append(self)
        try:
            temp_coffee=all_customers[self._name]
        except:
            print("user does not exist")
            all_customers[self._name]=[self._coffee_name]
        else:
            for x,coffee in enumerate(temp_coffee):
                if coffee == self._coffee_name:
                    break
                elif x == len(temp_coffee):
                    all_customers[self._name]=[temp_coffee,self._coffee_name]
    def set_price(self,price):
        price = float(input("Enter the price  "))
        if price <10 and price >1:
            self._price = price
        else :
            return "Invalid price (Price should be between 1 and 10"
    price = property(get_name,set_name)
    def customer():
        return self._name
    def coffee():
        return self._coffee_name
    def __str__(self):
        return "This is the Order"
        

