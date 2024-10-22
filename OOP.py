class Item:
#Add a class attribute
    pay_rate = 0.85
    payment_method = "card"
    #Create an empty list to store the items
    all_items = []

    # Constructor method to initialize the Item object with a name, price, and quantity
    def __init__(self, name, price, quantity):
        
        # Validate the input/arguments
        if name == "":
            raise ValueError("Name cannot be empty")
        if price <= 0:
            raise ValueError("Price must be greater than 0")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")

        # Assign the name of the item to the object attribute
        self.name = name
        
        # Assign the price of the item to the object attribute
        self.price = price
        
        # Assign the quantity of the item to the object attribute
        self.quantity = quantity

    def calculate_total_price(self):
        # Calculate the total price by multiplying the number of items (quantity)
        # by the cost of each item (price) and return the result
        return self.price * self.quantity
    
    def apply_discount(self):
        # Apply the discount to the price
        self.price = self.price * self.pay_rate


# Create an object
item1 = Item("Phone", 200, 3)
item2 = Item("Laptop", 2600,20)
item3 = Item("Light", 570,8)
item4 = Item("Cable", 100, 5)
item5 = Item("Pad", 200, 7)

 # Adding the instance to the class attribute list
Item.all_items.append(item1)
Item.all_items.append(item2)
Item.all_items.append(item3)
Item.all_items.append(item4)
Item.all_items.append(item5)

#Print list of items
#print(Item.all_items)

#Loop through the list of items and print the total price
for item in Item.all_items:
    print(item.calculate_total_price())

# Print the total price
print(item1.calculate_total_price())
print(item2.calculate_total_price())
print(Item.pay_rate)
print(item1.pay_rate)
print(item2.pay_rate)
print(Item.payment_method)
print(item1.payment_method)
item2.apply_discount()
item1.apply_discount()

print(item2.price)
print(item1.price)