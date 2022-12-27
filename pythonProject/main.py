import csv


class Item:
    discount = 0.2  # class attribute
    all = []

    def __init__(self, name: str, price: float, quantity):
        # Run validations to ensure that input arguments are valid.
        assert price >= 0, f"Price {price} not greater than or equal to 0."
        assert quantity >= 0, f"Quantity {quantity} is not valid input."

        # Instance Attributes: Assign attributes to object/instances.
        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * (1 - self.discount)
        # If discount is at class level - Item.discount, then we cannot overwrite discount at instance level.
        # If discount is accessed at instance level - self.discount, then we can overwrite discount at instance.

    def __repr__(self):  # Represents instance
        return f"{self.__class__.__name__}('{self.name},'{self.price}',{self.quantity})"
        # return f"Item ('{self.name}',{self.price},{self.quantity})"

    @classmethod
    def read_csv(cls):
        with open('items.csv', 'r') as file:
            reader = csv.DictReader(file)
            items = list(reader)

            for i in items:
                Item(
                    name=i['name'],
                    price=float(i['price']),
                    quantity=int(i['quantity'])
                )

    @staticmethod
    def check_if_quantity_is_integer(quantity):
        """
        Checks if an input is an integer and returns a boolean value.
        Both 5 and 5.0 will return True while 5.8 returns False.
        """
        if isinstance(quantity, float):
            return quantity.is_integer()
        elif isinstance(quantity, int):
            return True
        else:
            return False


# Inheritance
# Phone class will inherit all attributes from Item class.
class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # Call to super function inherits all attributes and methods from parent class.
        super().__init__(
            name,
            price,
            quantity
        )
        self.broken_phones = broken_phones

# item1 = Item('Phone', 100, 5)
# print(item1.name)

# name price and quantity are attributes of class object.
# functions inside classes are methods
# Python passes object itself as first argument

print(Item.discount)
# print(item1.__dict__)  # All attributes at the instance level.
# item1 cannot find discount as an attribute. But it finds the attribute at the instance level.

print(Item.__dict__)  # All attributes at class level

# item2 = Item('Laptop', 1000, 2)
# item2.discount = 0.3
# item2.apply_discount()
# print(item2.price)
# Overwrite discount at instance level.
# If we call print(item2.price) it will use class level discount of 20%.

# Create 3 more instances.
# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)

#  print(Item.all)  # List with 5 elements instances.
# for instance in Item.all:
#     print(instance.name)

Item.read_csv()
print(Item.all)
print(Item.check_if_quantity_is_integer(5.0))
print(Item.check_if_quantity_is_integer(2.4))
print(Item.check_if_quantity_is_integer(3))

phone1 = Phone("jscPhonev10", 500, 5, 1)
print(phone1)
print(Phone.all)
print(Item.all)