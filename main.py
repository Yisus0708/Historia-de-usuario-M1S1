continue_loop = True

while continue_loop:
    name = input("Product: ")

    # Validate price
    valid_price = False
    while not valid_price:
        try:
            price = float(input("Unit price: "))
            if price > 0:
                valid_price = True
            else:
                print("Enter a positive number.")
        except ValueError:
            print("Enter a valid number.")

    # Validate quantity
    valid_quantity = False
    while not valid_quantity:
        try:
            quantity = int(input("Quantity: "))
            if quantity > 0:
                valid_quantity = True
            else:
                print("Enter a positive integer.")
        except ValueError:
            print("Enter a valid integer.")

    # Calculate and show summary
    total_cost = price * quantity
    print(f"\nProduct: {name} | Price: {price} | Quantity: {quantity} | Total: {total_cost}\n")

    answer = input("Register another product? (yes/no): ").strip().lower()
    if answer == "no":
        continue_loop = False