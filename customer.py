class Customer:
    def __init__(self):
        name=str(input("Kindly enter your name   "))
        if (len(name)<=15 and len(name)>1):
            self._name = name
        else :
            raise ValueError ("Invalid name (name must be a between 1 and 15 characters)")
    def set_name(self):
        name=str(input("Kindly enter your name   "))
        if (len(name)<=15 and len(name)>1):
            self._name = name
        else :
            raise ValueError ("Invalid name (name must be a between 1 and 15 characters)")
    def get_name(self):
        return self._name
    name = property(set_name,get_name)
    def coffee(name):
        from order import all_customers
        return all_customers[name]
    def create_order(self,price,coffee):
        from Order import order
        new_order = Order(price,self._name,coffee)