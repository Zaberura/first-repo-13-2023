from datetime import date
from log_config import logged


class OutOfStockException(Exception):
    print("Аптека порожня")
    """Exception raised when the pharmacy is empty."""


class Medicine:
    """Class representing a medicine."""

    def __init__(self, name, price, quantity, is_prescription_needed, expiration_date):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.is_prescription_needed = is_prescription_needed
        self.expiration_date = expiration_date

    def __str__(self):
        return (f"{self.name}: Ціна - {self.price}, "
                f"Кількість - {self.quantity}, "
                f"Потрібен рецепт - {self.is_prescription_needed},"
                f" Термін придатності - {self.expiration_date}")


class Pharmacy:
    """Class representing a pharmacy."""

    def __init__(self):
        self.medicines = []

    def add_medicine(self, medicine):
        """Add a medicine to the pharmacy."""
        self.medicines.append(medicine)

    def remove_medicine(self, medicine):
        """Remove a medicine from the pharmacy."""
        self.medicines.remove(medicine)

    def check_expiration(self):
        """Check for expired medicines and remove them from the pharmacy."""
        today = date.today()
        expired_medicines = [med for med in self.medicines if med.expiration_date < today]
        for med in expired_medicines:
            self.remove_medicine(med)

    def apply_discount(self):
        """Apply a 10% discount to all medicines in the pharmacy."""
        for med in self.medicines:
            med.price *= 0.9

    def find_cheapest(self):
        """Find the cheapest medicine in the pharmacy."""
        if not self.medicines:
            return None
        cheapest = min(self.medicines, key=lambda med: med.price)
        return cheapest

    @logged(OutOfStockException, "console")
    def display_inventory(self):
        """Display the inventory of medicines in the pharmacy."""
        print("Аптека:")
        if not self.medicines:
            raise OutOfStockException("Аптека порожня")
        for med in self.medicines:
            print(med)

    def __del__(self):
        print("Аптеку було закрито.")


def main():
    """Main method"""
    pharmacy = Pharmacy()

    med1 = Medicine("Аспірин", 10, 100, False, date(2024, 12, 31))
    med2 = Medicine("Амоксицилін", 20, 50, True, date(2023, 5, 15))
    med3 = Medicine("Парацетамол", 5, 200, False, date(2025, 8, 20))

    pharmacy.add_medicine(med1)
    pharmacy.add_medicine(med2)
    pharmacy.add_medicine(med3)

    pharmacy.display_inventory()
    print("Знижка 10%:")
    pharmacy.apply_discount()
    pharmacy.display_inventory()

    print("Видалення прострочених ліків:")
    pharmacy.check_expiration()
    pharmacy.display_inventory()

    print("Знайдені найдешевші ліки:")
    cheapest = pharmacy.find_cheapest()
    if cheapest:
        print(cheapest)
    else:
        print("Аптека порожня.")


if __name__ == "__main__":
    main()
