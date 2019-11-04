# this function takes a dictionary as a parameter and totals up the number
# of items contained in a player's inventory.
def display_inventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print("Total number of items: " + str(item_total))

'''
This function returns a dictionary that represents the updated
inventory. All items from the dragon's loot are added to the main
inventory.
'''
def add_to_inventory(inventory, added_items):
    # return a dictionary that represents the updated inventory

    updated_inventory = dict(inventory)
    # loop through the list of dragon's items
    for item in added_items:
        updated_inventory.setdefault(item, 0)
        # increment the inventory count
        updated_inventory[item] += 1

    return updated_inventory




# define a dictionary containing all items in player's inventory
inventory = {'rope': 2, 'torch': 6, 'gold coin': 176, 'dagger': 1, 'arrow': 12}
# this is a vanquished dragon's loot, represented as a list of strings
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inventory = add_to_inventory(inventory, dragon_loot)
display_inventory(inventory)
