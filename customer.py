from order import all_customers
class Customer:
    def __init__(name,self):
        self._name=name
    def set_name(self,name):
        name=str(input("Kindly enter your name   "))
        if (len(name)<=15 and len(name)>1):
            self._name = name
        else :
            return ("Invalid name (name must be a between 1 and 15 characters)")
    def get_name(self):
        return self._name
    name = property(set_name,get_name)
    def coffee(name):
        return all_customers[name]



