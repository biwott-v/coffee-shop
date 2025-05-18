class Coffee:
    def __init__(self,name):
        self._name=name
    def set_name(name):
        name = str(input("Enter a coffee name"))
        if len(name) >= 3:
            self_name=name
        else :
            return "Invalid coffee name (name must have at least than 3 characters)"
    def get_name():
        return self._name
    name = property(get_name,set_name)