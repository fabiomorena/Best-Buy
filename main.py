import products
import store


def list_all_products(store_obj):
    """Lists all active products in the store."""
    print("\n------ Available Products ------")
    active_products = store_obj.get_all_products()
    if not active_products:
        print("No products in the store at the moment.")
    else:
        for i, product in enumerate(active_products, 1):
            print(f"{i}. ", end="")
            product.show()
    print("----------------------------\n")


def show_total_amount(store_obj):
    """Shows the total number of all items in the store."""
    total_quantity = store_obj.get_total_quantity()
    print(f"\nTotal items in store: {total_quantity}\n")


def make_an_order(store_obj):
    """Guides the user through making an order."""
    all_products = store_obj.get_all_products()
    if not all_products:
        print("Sorry, there are no products available to order.\n")
        return

    print("\n--- Start New Order ---")
    list_all_products(store_obj)

    shopping_list = []
    while True:
        try:
            product_choice = input("Enter product number to order (or 'done' to finish): ")
            if product_choice.lower() == 'done':
                break

            product_index = int(product_choice) - 1
            if not (0 <= product_index < len(all_products)):
                print("Error: Invalid product number.\n")
                continue

            chosen_product = all_products[product_index]

            quantity_choice = input(f"Enter quantity for '{chosen_product.name}': ")
            quantity = int(quantity_choice)
            if quantity <= 0:
                print("Error: Quantity must be a positive number.\n")
                continue

            # Add valid item to shopping list
            shopping_list.append((chosen_product, quantity))
            print(f"Added {quantity} of '{chosen_product.name}' to your order.\n")

        except ValueError:
            print("Error: Invalid input. Please enter a number.\n")
        except Exception as e:
            print(f"An error occurred: {e}\n")

    if not shopping_list:
        print("Order cancelled. No items were selected.\n")
        return

    print("\n--- Finalizing Order ---")
    try:
        total_cost = store_obj.order(shopping_list)
        print(f"Order successful! Total cost: ${total_cost:.2f}\n")
    except Exception as e:
        # The .buy() method will raise an exception for insufficient stock
        print(f"Error: Your order could not be processed. Reason: {e}\n")


def start(store_obj):
    """Runs the main interactive loop for the store."""
    while True:
        print("********** Store Menu **********")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")
        print("******************************")

        choice = input("Please choose a number: ")

        if choice == '1':
            list_all_products(store_obj)
        elif choice == '2':
            show_total_amount(store_obj)
        elif choice == '3':
            make_an_order(store_obj)
        elif choice == '4':
            print("Thank you for visiting. Goodbye! ")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.\n")


def main():
    """Main entry point of the program."""
    # Setup initial stock of inventory
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250)
    ]
    best_buy = store.Store(product_list)

    # Start the user interface
    start(best_buy)


if __name__ == "__main__":
    main()