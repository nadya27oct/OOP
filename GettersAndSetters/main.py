from item import Item
from phone import Phone

Item.read_csv()

print(Item.all)

item1 = Item('My Item', 750, 2)
print(item1.name)

# If below command is run before specifying a name.setter in Item class,
# we get an attribute error saying cannot set attribute name.
item1.name = "Other Item"
print(item1.name)

item1.name = "Additional Item"
print(item1.name)

