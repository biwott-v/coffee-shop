from customer import Customer
from coffee import Coffee

class Order(Customer,Coffee):
    all_coffee,temp_coffee=[],[]
    all_customers={}
    def __init__(self):
        Customer.__init__(self)
        Coffee.__init__(self)
        price = float(input("Enter the price  "))
        if price <10 and price >1:
            self._price = price
        else :
            raise ValueError ("Name must be between 1 and 15 characters")
        Order.all_coffee.append(self)
        try:
            temp_coffee=Order.all_customers[self._name]
        except:
            print("user does not exist")
            Order.all_customers[self._name]=[self._coffee_name]
        else:
            for x,coffee in enumerate(temp_coffee):
                if coffee == self._coffee_name:
                    break
                elif x == len(temp_coffee):
                    Order.all_customers[self._name]=[temp_coffee,self._coffee_name]
    def set_price(self,price):
        price = float(input("Enter the price  "))
        if price <10 and price >1:
            self._price = price
        else :
            raise ValueError ("Name must be between 1 and 15 characters")
    def get_price():
        return self._price
    price = property(get_price,set_price)
    def customer():
        return self._name
    def coffee():
        return self._coffee_name
    def __str__(self):
        return "{0} ordered {1} which costs {2}".format(self._name,self._coffee_name,self._price)
        

victor = Order()
print(victor)