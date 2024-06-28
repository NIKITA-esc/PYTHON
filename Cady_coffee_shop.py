def menu():
    item1 = {
        "espresso": 5.00,
        "americano": 5.00,
        "filter coffee": 5.00,
        "latte": 6.25,
        "cappuccino": 6.35,
        "macchiato": 6.35,
        "mocha": 6.35,
        "cold brew": 6.89,
    }
    item2 = {
        "iced caramel macchiato": 7.25,
        "dragon drink": 7.30,
        "vanilla sweet cream nitro cold brew": 7.50,
        "honey citrus mint tea": 8.00,
    }
    
    print(" Regular drinks: ")
    for item, price in item1.items():
        print(f"- {item.title()}: ${price:.2f}")

    print("\nSpecial drinks: ")
    for item, price in item2.items():
        print(f"- {item.title()}: ${price:.2f}")

    return item1, item2

def main():
    item1, item2 = menu()
    order_price = 0
    while True:
        order = input("\nHi! What would you like to have today?\nEnter your order: ").strip().lower()
        if order in item1:
            print("Your order has been added")
            order_price += item1[order]
        elif order in item2:
            print("Your order has been added")
            order_price += item2[order]
        else:
            print("Enter correct choice")
            continue

        order_more = input("Would you like to order more? Enter yes/no: ").strip().lower()
        if order_more != "yes":
            break

    print(f"Thank you, Enjoy your drink. You have to pay ${order_price:.2f} for your drink(s).")

if __name__ == "__main__":
    main()

