# demonstrates nested dictionaries
# let's see who is bringing what to a picnic
all_guests = {'Alice': {'apples': 5, 'pretzels': 48},
            'Bob': {'egg salad sandwiches': 4, 'pears': 2},
            'Lisa': {'cups': 3, 'apple pies': 1}}

def total_brought(guests, item):
    num_brought = 0
    # iterate over the key, value pairs in guests
    for k, v in guests.items():
        # get method takes 2 arguments: the key of the value to retrieve,
        # and a fallback value to return if key does not exist.
        num_brought = num_brought + v.get(item, 0)
    return num_brought


print('Number of things being brought:')
print(' - Apples ' + str(total_brought(all_guests, 'apples')))
print(' - Pretzels ' + str(total_brought(all_guests, 'pretzels')))
print(' - Egg Salad Sandwiches ' + str(total_brought(all_guests, 'egg salad sandwiches')))
print(' - Cakes ' + str(total_brought(all_guests, 'cakes')))
print(' - Pears ' + str(total_brought(all_guests, 'pears')))
print(' - Cups ' + str(total_brought(all_guests, 'cups')))
print(' - Apple Pies ' + str(total_brought(all_guests, 'apple pies')))
