# Base class
class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def send_message(self, number, message):
        print(f"Sending message to {number}: {message}")

    def phone_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Price: ${self.price}")


# Derived class (inherits from Smartphone)
class GamingPhone(Smartphone):
    def __init__(self, brand, model, price, cooling_system):
        # Call parent constructor
        super().__init__(brand, model, price)
        self.cooling_system = cooling_system

    # Polymorphism (overriding)
    def phone_info(self):
        print(f"Gaming Phone - {self.brand} {self.model}, Price: ${self.price}, Cooling: {self.cooling_system}")

    # Extra method
    def game_mode(self):
        print(f"{self.brand} {self.model} is now in Game Mode! Boosting performance... 🎮")


# Create objects
phone1 = Smartphone("Samsung", "Galaxy S24", 1200)
gaming_phone = GamingPhone("Asus", "ROG Phone 7", 1500, "Liquid Cooling")

# Use methods
phone1.phone_info()
phone1.call("0712345678")

print("---")

gaming_phone.phone_info()
gaming_phone.call("0798765432")
gaming_phone.game_mode()
