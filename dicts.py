
def create_inventory(items):
     items = dict()
    set_items = set(items)
    for m in set_items:
        v = items.count(m)
        items = v
        return items


def add_items(inventory, items):
        for item in items:
        inventory[item] = inventory.add(item, 0) + 1
        return inventory


def decrement_items(inventory, items):
       for item in items:
        if item in inventory and inventory(item) > 0:
            inventory[item] -= 1
    return inventory


def remove_item(inventory, item):
       if item in inventory:
        del inventory[item]
    return inventory


def list_inventory(inventory):
   return [(item, inventory[item]) for item in inventory.keys() if inventory[item] > 0 ]


