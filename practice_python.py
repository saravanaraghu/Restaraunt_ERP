def calculate_bill(price, quantity):
    total = price * quantity
    return total

def calculate_gst(bill_amount, gst_rate):
    gst_amount = bill_amount * (gst_rate / 100)
    return gst_amount

price = 100
quantity = 2
bill_amount = calculate_bill(price, quantity)
gst_rate = 5
gst_amount = calculate_gst(bill_amount, gst_rate)
print(f"Bill Amount: {bill_amount}")
print(f"GST Amount: {gst_amount}")