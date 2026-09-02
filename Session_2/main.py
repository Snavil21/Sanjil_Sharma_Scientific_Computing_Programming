from coffee_shop.shop import CoffeeShop

def main():
    shop = CoffeeShop()                                                   # How do we initialize an object here?

    print("☕ Welcome to Our Coffee Shop! ☕")

    shop.display_menu()                                         # Why am i not storing it in a variable here?
                                                                # Answer here: Because display_menu takes self as variable, so not need to store in another variable.

    category = input("\nChoose a category: ").lower()

    shop.display_category(category)

    item = input("\nChoose an item: ").lower()
    quantity = int(input("Enter quantity: "))

    total = shop.order(category, item, quantity)

    if total is not None:
        print("\n--------------------------")
        print(f"Item     : {item.title()}")
        print(f"Quantity : {quantity}")
        print("Total    : ₹",shop.order(category,item,quantity))                                   # How to print the total here?
        print("--------------------------")
        print("Thank you for your order! 😊")

if __name__ == "__main__":
    main()
