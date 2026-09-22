menu_items = {}
daily_sales = []

def add_item(item_name, item_price):
    if item_name in menu_items:
        print("Item already exists. Updating the price.")
    menu_items[item_name] = item_price


def view_items():
    print("The Items present in the menu are:")
    count = 1
    for item, price in menu_items.items():
        print(f"{count}. {item}: ₹{price}")
        count += 1
        
def calculate_bill(item_name, quantity):
    if item_name in menu_items:
        price = menu_items[item_name]
        total_bill = price * quantity
        total_gst = total_bill * 0.05  # Assuming GST is 5%
        return total_bill, total_gst
    else:
        print("Item not found in the menu.")
        return None, None
    
def daily_sales_report(daily_sales):
    print("Daily Sales Report:")
    for item, quantity, amount in daily_sales:
        print(f"Item: {item}, Quantity: {quantity}, Amount: {amount}")
    total_sales = sum(amount for _, _, amount in daily_sales)
    print(f"Total Sales: {total_sales}")
    
def exit_program():
    print("Exiting...")
    exit()
    
while True:
    print("1. Add item")
    print("2. View items")
    print("3. Calculate bill")
    print("4. Daily sales report")
    print("5. Exit")
    
    try:
        choice = int(input("Enter your choice: "))
    except ValueError as e:
        print("Please enter a valid number from 1 to 5.")
        continue

    if choice == 1:
        item_name = input("Enter item name:").strip().title()
        item_price = float(input("Enter item price:"))
        add_item(item_name, item_price)
    elif choice == 2:
        view_items()
    elif choice == 3:
        menu_item = input("Enter the item name to calculate bill:")
        quantity = int(input("Enter the quantity:"))
        total_bill, gst_amount = calculate_bill(menu_item, quantity)
        if total_bill is not None:
            print(f"Total Bill Amount: {total_bill}")
            print(f"GST Amount: {gst_amount}")
            print(f"Total Amount: {total_bill + gst_amount}")
            daily_sales.append((menu_item, quantity, total_bill + gst_amount))
    elif choice == 4:
        daily_sales_report(daily_sales)
    elif choice == 5:
        exit_program()