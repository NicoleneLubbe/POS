# Define the product
products = {
    "Kaas": 50.00,
    "Melk": 30.00,
    "Brood": 15.00
}

# Function to display the product list
def display_products():
    print("Product:")
    for product, price in products.items():
        print(f"{product} R{price:.2f}")

# Function to calculate the total
def calculate_total(cart):
    total = sum(products[product] for product in cart)
    return total

# Function to run the POS system
def run_pos_system():
    cart = []
    while True:
        display_products()
        print("Add a product to the cart, or type 'Exit' to leave.")
        choice = input("Product name: ").capitalize()

        if choice == "Exit":
            break
        elif choice in products:
            cart.append(choice)
        else:
            print("Unavailable product.")

    total = calculate_total(cart)
    print("\Cart:")
    for product in cart:
        print(product)

    print(f"Total: R{total:.2f}")

# Run the POS system
if __name__ == "__main__":
    run_pos_system()
