class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.is_available = True

    def display(self):
        availability = "Available" if self.is_available else "Not Available"
        print(
            f"Item name : {self.name}, Price: ₹{self.price:.2f}, Availability: {availability}"
        )
        
    def update_price(self, new_price):
        if new_price <= 0:
            print("Price must be greater than zero.")
        else:
            old_price = self.price
            self.price = new_price
            print(
                f"Updated {self.name} price from ₹{old_price:.2f} to ₹{new_price:.2f}. and the price is updated successfully."
            )
            
    def mark_unavailable(self):
        self.is_available = False
        print(f"{self.name} is now marked as unavailable.")
briyani = MenuItem("Briyani", 150)
briyani.display()  # Output: Briyani: ₹150.00 - Available
briyani.update_price(160)  # Output: Updated Briyani price from ₹150.00 to ₹160.00. and the price is updated successfully.
briyani.mark_unavailable()  # Output: Briyani is now marked as unavailable.
briyani.display()  # Output: Briyani: ₹160.00 - Not Available