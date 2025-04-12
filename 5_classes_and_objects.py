#  type: ignore
class InventoryItem:
    custom_static_var = "This is static var not instance member"
    active_instances = 0

    # ctor
    def __init__(self, item_name: str, quantity: int, unit_cost: float):
        self.item_name = item_name
        self.quantity = quantity
        self.unit_cost = unit_cost
        InventoryItem.active_instances += 1

    def __del__(self):
        InventoryItem.active_instances -= 1

    def get_details(self) -> str:
        return f"Item: {self.item_name}, Quantity: {self.quantity}, Unit Cost: ${self.unit_cost:.2f}"

    def adjust_quantity(self, change: int):
        if self.quantity + change >= 0:
            self.quantity += change

    def calculate_total_value(self) -> float:
        return self.quantity * self.unit_cost

    def __str__(self) -> str:
        # User-friendly string representation.
        return f"{self.item_name} (Qty: {self.quantity})"

    def __repr__(self) -> str:
        # Provides enough information to recreate the object or understand its state during debugging.
        return f"InventoryItem(item_name='{self.item_name}', quantity={self.quantity}, unit_cost={self.unit_cost})"


print(InventoryItem.custom_static_var)

a = InventoryItem("Apples", 10, unit_cost=1.0)
o = InventoryItem("Oranges", 10, unit_cost=1.0)
a.adjust_quantity(-2)

print(a, "\n", o, sep="")

# add instance var in runtime
a.desc = "Apples are from Spain"
print(a.desc)

# how often this will be useful ? we will see
aa = eval(repr(a))
a.adjust_quantity(+10)

print(a)
print(aa)

print(f"Active instances count {InventoryItem.active_instances}")
del aa
print(f"Active instances count {InventoryItem.active_instances}")
del a, o
print(f"Active instances count {InventoryItem.active_instances}")
