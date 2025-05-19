class Coffee:
    def __init__(self):
        coffee_name = str(input("Enter a coffee name"))
        if len(coffee_name) >= 3:
            self._coffee_name=coffee_name
        else :
            raise ValueError ("Invalid coffee name (name must have at least than 3 characters")
    def set_coffee_name(coffee_name):
        coffee_name = str(input("Enter a coffee name"))
        if len(coffee_name) >= 3:
            self._coffee_name=coffee_name
        else :
            raise ValueError ("Invalid coffee name (name must have at least than 3 characters")
    def get_coffee_name():
        return self._coffee_name
    coffee_name = property(get_coffee_name,set_coffee_name)
    def order():
        from order import all_cofee
        return all_coffee
    def customer():
        from order import all_customers
        customers=[]
        for customer in all_customers.keys():
            customers.append(customer)
        return customers
    def num_orders(coffee):
        pass

