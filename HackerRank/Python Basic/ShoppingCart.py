class Item:
    # Item class to hold name and price of each item
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add(self, item):
        # Add the item to the shopping cart
        self.items.append(item)

    def total(self):
        # Calculate and print the total price of items in the cart
        print(sum(item.price for item in self.items))

    def len(self):
        # Print the number of items in the cart
        print(len(self.items))


if __name__ == '__main__':
    n = int(input())  # Number of items to be created
    cart = ShoppingCart()

    # Dictionary to store the created items by name
    available_items = {}

    # Creating items and storing them in the dictionary
    for i in range(n):
        name = input()
        price = int(input())
        item = Item(name, price)
        available_items[name] = item  # Store item with name as the key

    q = int(input())  # Number of queries
    for i in range(q):
        # Split the query to handle both 'add <item_name>' and method calls
        query = input().split()

        if query[0] == "total":
            cart.total()  # Call the total method to print the total price
        elif query[0] == "len":
            cart.len()  # Call the len method to print the number of items
        elif query[0] == "add":
            item_name = query[1]
            if item_name in available_items:
                # Add the item to the cart
                print(available_items[item_name])
                cart.add(available_items[item_name])
