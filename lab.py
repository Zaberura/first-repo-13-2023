from datetime import date

class Medicine:    def __init__(self, name, price, quantity, is_prescription_needed, expiration_date):
        self.name = name        self.price = price
        self.quantity = quantity        self.is_prescription_needed = is_prescription_needed
        self.expiration_date = expiration_date
        
    def display_info(self):        print(f"Medicine: {self.name}, Price: {self.price}, Quantity: {self.quantity}, Prescription: {self.is_prescription_needed}, Expiration Date: {self.expiration_date}")
class Pharmacy:
        
    def __init__(self):        self.medicines = []
    def add_medicine(self, medicine):
        self.medicines.append(medicine)
    def remove_medicine(self, medicine_name):        self.medicines = [med for med in self.medicines if med.name != medicine_name]
    def check_expiration(self):
        today = date.today()        self.medicines = [med for med in self.medicines if med.expiration_date >= today]
    def apply_discount(self):
        for med in self.medicines:            med.price -= 0.1 * med.price
    def display_cheapest_medicines(self):
        cheapest_medicines = sorted(self.medicines, key=lambda x: x.price)[:5]        print("Cheapest Medicines:")
        for med in cheapest_medicines:            med.display_info()
    def display_inventory(self):
        print("Pharmacy Inventory:")        for med in self.medicines:
            med.display_info()
# Example usage in the main methoddef main():
    medicine1 = Medicine("Paracetamol", 5.0, 100, False, date(2024, 12, 31))    medicine2 = Medicine("Aspirin", 3.5, 50, True, date(2023, 6, 30))
    medicine3 = Medicine("Ibuprofen", 8.0, 75, False, date(2023, 8, 15))
    pharmacy = Pharmacy()    pharmacy.add_medicine(medicine1)
    pharmacy.add_medicine(medicine2)
    pharmacy.add_medicine(medicine3)
    pharmacy.display_inventory()
    pharmacy.apply_discount()    print("\nAfter Applying Discount:")
    pharmacy.display_inventory()
    pharmacy.check_expiration()    print("\nAfter Checking Expiration:")
    pharmacy.display_inventory()
    pharmacy.display_cheapest_medicines()
    pharmacy.remove_medicine("Aspirin")    print("\nAfter Removing Aspirin:")
    pharmacy.display_inventory()
if name == "__main__":
    main()
