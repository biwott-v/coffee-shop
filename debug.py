from customer import Customer
from order import Order
from coffee import Coffee

#A new Order
def new_order(my_order):
    my_order = Order()
    return my_order


if __name__ == "__main__":
    guest=""
    print(new_order(guest))