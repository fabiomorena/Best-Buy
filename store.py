import products
from typing import List, Tuple


class Store:
    """
    Represents a store that holds a list of products and can process orders.
    """

    def __init__(self, list_of_products: List[products.Product]):
        """Initializes a Store instance with a list of products."""
        self.products = list_of_products if list_of_products else []

    def add_product(self, product: products.Product):
        """Adds a product to the store's inventory."""
        self.products.append(product)

    def remove_product(self, product: products.Product):
        """Removes a product from the store's inventory."""
        if product in self.products:
            self.products.remove(product)
        else:
            print(f"Error: Product {product.name} not found in store.")

    def get_total_quantity(self) -> int:
        """Returns the total count of all items in the store."""
        total_quantity = 0
        for product in self.products:
            total_quantity += product.get_quantity()
        return total_quantity

    def get_all_products(self) -> List[products.Product]:
        """Returns a list of all active products in the store."""
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list: List[Tuple[products.Product, int]]) -> float:
        """
        Processes an order from a shopping list.
        The shopping list is a list of (product, quantity) tuples.
        Returns the total cost of the order.
        """
        total_cost = 0.0
        for product_to_buy, quantity in shopping_list:
            try:
                # The product's 'buy' method handles stock checks and exceptions
                item_cost = product_to_buy.buy(quantity)
                total_cost += item_cost
            except Exception as e:
                print(f"Order failed for {product_to_buy.name}: {e}")
                # In a real-world scenario, you might implement transaction
                # logic to roll back the entire order if one item fails.
                # For this exercise, we let the exception halt the process.
                raise
        return total_cost


def main():
    """Function to test the Store class."""
    # Setup the store with a list of products
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]
    best_buy = Store(product_list)

    # 1. Test getting total quantity
    print("--- Initial Store State ---")
    print(f"Total items in store: {best_buy.get_total_quantity()}")

    # 2. Test getting all active products
    all_products = best_buy.get_all_products()
    print("Available products:")
    for prod in all_products:
        prod.show()

    # 3. Test ordering products
    print("\n--- Placing an Order ---")
    # Note: The test code uses `products` as the variable name.
    products_to_order = best_buy.get_all_products()

    # We create an order list with (product, quantity)
    order_list = [(products_to_order[0], 1), (products_to_order[1], 2)]

    try:
        total_price = best_buy.order(order_list)
        print(f"Total order cost: ${total_price}")
    except Exception as e:
        print(f"Could not complete the order. Reason: {e}")

    print("\n--- Final Store State ---")
    print(f"Total items in store: {best_buy.get_total_quantity()}")


if __name__ == "__main__":
    # Ensure products.py is in the same directory or accessible
    main()