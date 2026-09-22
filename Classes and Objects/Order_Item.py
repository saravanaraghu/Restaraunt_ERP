from menu_item_practice import MenuItem

class OrderItem:
    def __init__(self, menu_item, quantity):
        self.menu_item = menu_item
        if(quantity > 0):
            self.quantity = quantity
        else:
            print("Quantity must be a positive integer.")
