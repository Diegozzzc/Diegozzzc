class Order:

    def __init__(self, qtty, customer):
        self.customer = customer
        self.qtty = qtty

    def print(self):
        print("     Cliente:", self.customer)
        print("     Cantidad:", self.qtty)
        print("                             --")

    def get_qtty(self):
        return self.qtty

    def get_customer(self):
        return self.customer
