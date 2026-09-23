from menu_item_practice import MenuItem


class OrderItem:
    def __init__(self, menu_item, quantity):
        self.menu_item = menu_item
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer.")
        if quantity < 1:
            raise ValueError("Quantity must be a positive integer.")
        self.quantity = quantity

    def line_total(self):
        return self.menu_item.price * self.quantity

    def display(self):
        return f"{self.menu_item.name}\nQty: {self.quantity}\nPrice: {self.menu_item.price}\nTotal: {self.line_total()}"
    
    


if __name__ == "__main__":
    # Example usage
    item = MenuItem("Burger", 5.99)
    order_item = OrderItem(item, 2)

    print(order_item.display())
    print(f"Line Total: {order_item.line_total()}")
