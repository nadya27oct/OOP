import csv


class Item:
    discount = 0.2  # class attribute
    all = []

    def __init__(self, name: str, price: float, quantity):
        # Run validations to ensure that input arguments are valid.
        assert price >= 0, f"Price {price} not greater than or equal to 0."
        assert quantity >= 0, f"Quantity {quantity} is not valid input."

        # Instance Attributes: Assign attributes to object/instances.
        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    @property
    # Property Decorator = Read Only Attribute
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("Name is too long")
        else:
            self.__name = value

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
