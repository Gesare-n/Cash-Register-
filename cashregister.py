class CashRegister:
    def __init__(self):
        # Initialize attributes to keep track of items, total price, and the last transaction
        self.items = []
        self.total_price = 0
        self.last_transaction = None

    def add_item(self, item, quantity, price):
        # Add an item to the register
        self.items.append({'item': item, 'quantity': quantity, 'price': price})
        # Update the total price by multiplying quantity with price
        self.total_price += quantity * price
        # Update the last transaction details
        self.last_transaction = {'item': item, 'quantity': quantity, 'price': quantity * price}

    def calculate_discount(self, percentage):
        # Calculate discount based on a percentage of the total price
        discount = self.total_price * (percentage / 100)
        # Reduce the total price by the discount amount
        self.total_price -= discount
        # Update the last transaction with discount information
        self.last_transaction['discount'] = discount

    def void_last_transaction(self):
        if self.last_transaction:
            # Retrieve details of the last transaction
            item = self.last_transaction['item']
            quantity = self.last_transaction['quantity']
            price = self.last_transaction['price']
            # Deduct the price of the last transaction from the total price
            self.total_price -= price
            # Remove the last transaction item from the items list
            self.items = [i for i in self.items if i['item'] != item]
            # Reset last transaction details
            self.last_transaction = None

    def get_receipt(self):
        receipt = []
        # Generate receipt for each item in the items list
        for item in self.items:
            receipt.append(f"{item['item']}: {item['quantity']} x ${item['price']} = ${item['quantity'] * item['price']}")
        # Check if there was a discount applied in the last transaction
        if self.last_transaction and 'discount' in self.last_transaction:
            receipt.append(f"Discount: -${self.last_transaction['discount']}")
        # Add total price to the receipt
        receipt.append(f"Total: ${self.total_price}")
        return receipt
