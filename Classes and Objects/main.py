from Order_Item import OrderItem
from menu_item_practice import MenuItem

briyani = MenuItem("Briyani", 12.99)
masala_dosa = MenuItem("Masala Dosa", 8.99)
Coffee = MenuItem("Coffee", 3.99)

order_item1 = OrderItem(briyani, 2)
order_item2 = OrderItem(masala_dosa, 3)
order_item3 = OrderItem(Coffee, 1)

print(order_item1.display())
print(order_item2.display())
print(order_item3.display())

sum_total = 0

for order_item in [order_item1, order_item2, order_item3]:
    sum_total += order_item.line_total()

print(f"Total Order Amount: {sum_total:.2f}")

gst_rate = float(input("Enter GST rate (in percentage): "))
gst_amount = (sum_total * gst_rate) / 100
final_amount = sum_total + gst_amount
print(f"GST Amount: {gst_amount:.2f}")
print(f"Final Amount (including GST): {final_amount:.2f}")
