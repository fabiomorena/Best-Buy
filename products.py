class Product:
    """
    Represents a product with a name, price, and quantity.
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
        Initializes a Product instance.
        Raises ValueError if the name is empty, or if price/quantity are negative.
        """
        if not name:
            raise ValueError("Product name cannot be empty.")
        if price < 0 or quantity < 0:
            raise ValueError("Price and quantity must be non-negative.")

        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)
        self.active = True

    def get_quantity(self) -> int:
        """Returns the current quantity of the product."""
        return self.quantity

    def set_quantity(self, quantity: int):
        """
        Sets the product's quantity.
        If the quantity is 0, the product is deactivated.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """Returns True if the product is active, False otherwise."""
        return self.active

    def activate(self):
        """Activates the product, making it available for purchase."""
        self.active = True

    def deactivate(self):
        """Deactivates the product, making it unavailable for purchase."""
        self.active = False

    def show(self):
        """Prints the product's details."""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity: int) -> float:
        """
        Processes a purchase of a given quantity.
        Returns the total price for the purchase.
        Raises Exception if the product is inactive or there's insufficient stock.
        """
        if not self.is_active():
            raise Exception(f"Product '{self.name}' is not currently for sale.")
        if quantity <= 0:
            raise ValueError("Quantity to buy must be a positive number.")
        if quantity > self.quantity:
            raise Exception(f"Not enough stock for '{self.name}'. "
                            f"Requested: {quantity}, Available: {self.quantity}")

        total_price = quantity * self.price
        # Use the setter to update quantity, which handles deactivation
        self.set_quantity(self.quantity - quantity)
        return total_price


def main():
    """Function to test the Product class."""
    try:
        print("--- Initializing Products ---")
        bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
        mac = Product("MacBook Air M2", price=1450, quantity=100)
        bose.show()
        mac.show()

        print("\n--- Processing Purchases ---")
        print(f"Cost of 50 Bose earbuds: ${bose.buy(50)}")
        print(f"Cost of 100 MacBooks: ${mac.buy(100)}")

        print(f"\nIs the MacBook active after selling out? {mac.is_active()}")

        print("\n--- Final Product Status ---")
        bose.show()
        mac.show()

        print("\n--- Restocking Product ---")
        bose.set_quantity(1000)
        bose.show()

    except (ValueError, Exception) as e:
        print(f"\nAn error occurred: {e}")


if __name__ == "__main__":
    main()