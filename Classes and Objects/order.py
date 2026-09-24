from order_item import OrderItem
from menu_item_practice import MenuItem


class Order:
    order_counter = 1000

    def __init__(self, table_number, gst_rate=5):
        Order.order_counter = Order.order_counter + 1
        self.order_id = f"ORD-{Order.order_counter}"
        self.table_number = table_number
        self.order_items = []
        self.gst_rate = gst_rate

    def add_order_item(self, order_item):
        if not isinstance(order_item, OrderItem):
            raise TypeError(f"{order_item} is not an instance of OrderItem.")
        self.order_items.append(order_item)

    def remove_order_item(self, order_item):
        if not isinstance(order_item, OrderItem):
            raise TypeError(f"{order_item} is not an instance of OrderItem.")
        elif order_item in self.order_items:
            self.order_items.remove(order_item)
        else:
            raise ValueError(f"{order_item} is not in the order items list.")

    def calculate_subtotal(self):
        total = 0
        for order_item in self.order_items:
            total += order_item.calculate_subtotal()
        return total

    def calculate_gst(self):
        return (self.calculate_subtotal() * self.gst_rate) / 100

    def calculate_total(self):
        return self.calculate_subtotal() + self.calculate_gst()

    def display_order(self):
        if not self.order_items:
            return(
                f"Order ID: {self.order_counter}\n"
                
            )
        lines = []
        lines.append("========== Restaurant Bill ==========")
        lines.append(f"Order Number: {self.order_counter}")
        lines.append(f"Table Number: {self.table_number}")
        for order_item in self.order_items:
            lines.append(
                f"{order_item.menu_item.name} X {order_item.quantity} = {order_item.calculate_subtotal():.2f}"
            )
        lines.append("")
        lines.append(f"Subtotal: {self.calculate_subtotal():.2f}")
        lines.append(f"GST ({self.gst_rate})%: {self.calculate_gst():.2f}")
        lines.append(f"Grand Total: {self.calculate_total():.2f}")

        return "\n".join(lines)


if __name__ == "__main__":
    briyani = MenuItem("Briyani", 220)
    burger = MenuItem("Burger", 159)
    order_for_table_1 = OrderItem(briyani, 5)
    order_for_table_2 = OrderItem(burger, 7)
    orders = Order(1)
    orders.add_order_item(order_for_table_1)
    orders.add_order_item(order_for_table_2)
    print(orders.display_order())
    orders.remove_order_item(order_for_table_2)
    print("\nAfter removing Burger:\n")
    orders.display_order()
    print(orders.calculate_gst())
    print(orders.calculate_total())
    orders_1 = Order(2, 18)
    orders_1.add_order_item(order_for_table_1)
    print(orders_1.display_order())
    print(orders.order_id)
    print(orders_1.order_id)
