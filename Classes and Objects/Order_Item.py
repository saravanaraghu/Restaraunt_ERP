from copy import error

from menu_item_practice import MenuItem


class OrderItem:
    def __init__(self, menu_item, quantity):
        if menu_item is None:
            raise ValueError("Menu item cannot be None.")
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer.")
        if quantity < 1:
            raise ValueError("Quantity must be a positive integer.")
        self.menu_item = menu_item
        self.quantity = quantity

    def calculate_subtotal(self):
        return self.menu_item.price * self.quantity
         
    def display(self):
        return f"{self.menu_item.name}\nQty: {self.quantity}\nPrice: {self.menu_item.price:.2f}\nTotal: {self.calculate_subtotal():.2f}"
    
    def total_display(self):
        return f"{self.menu_item.name} X {self.quantity} = ₹ {self.calculate_subtotal():.2f}"
    

if __name__ == "__main__":
    item = MenuItem("Pizza", 250.0)
    try:
        order_item = OrderItem(item, 0)
        order_item.display()

    except ValueError as error:
        print(error)    

    print(order_item.display())
    print(f"Line Total: {order_item.calculate_subtotal()}")
    print(order_item.total_display())