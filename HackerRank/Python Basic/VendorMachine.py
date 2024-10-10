
class VendingMachine:
    # Implement the VendingMachine here
    def __init__(self, num_items, item_price):
        self.num_items = num_items
        self.item_price = item_price

    def buy(self, req_items, money):
        required_money = self.item_price * req_items
        if self.num_items >= req_items and money >= required_money:
            self.num_items -= req_items
            print(money-required_money)
        elif (self.num_items < req_items):
            print("Not enough items in the machine")
        elif (money < required_money):
            print("Not enough coins")


if __name__ == '__main__':
    num_items, item_price = map(int, input().split())
    VM = VendingMachine(num_items, item_price)
    n = int(input())
    for i in range(n):
        req_items, money = map(int, input().split())
        VM.buy(req_items, money)
