menu_items = {}

calculate_bill = lambda price, quantity: price * quantity
calculate_gst = lambda amount, rate: amount * rate / 100

daily_sales = []


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
        if item_name in menu_items:
            print("Item already exists. Updating the price.")
        menu_items[item_name] = item_price
    elif choice == 2:
        print("Items in the list:")
        count = 1
        for item, price in menu_items.items():
            print(f"{count}. {item} - ₹{price}")
            count += 1
    elif choice == 3:
        menu_item = input("Enter the item name to calculate bill:")
        quantity = int(input("Enter the quantity:"))
        if menu_item in menu_items:
            price = menu_items[menu_item]
            total_bill = calculate_bill(price, quantity)
            gst_rate = 5
            gst_amount = calculate_gst(total_bill, gst_rate)
            print(f"Total Bill Amount: {total_bill}")
            print(f"GST Amount: {gst_amount}")
            print(f"Total Amount: {total_bill + gst_amount}")
            daily_sales.append((menu_item, quantity, total_bill + gst_amount))
    elif choice == 4:
        print("Daily Sales Report:")
        for item, quantity, amount in daily_sales:
            print(f"Item: {item}, Quantity: {quantity}, Amount: {amount}")
        total_sales = sum(amount[2] for amount in daily_sales)
        print(f"Total Sales: {total_sales}")
    elif choice == 5:
        print("Exiting...")
        break
