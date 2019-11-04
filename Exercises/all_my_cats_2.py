cat_names = []

while True:
    name = input('Enter the name of cat ' + str(len(cat_names) + 1) +
    ' (Or simply press Enter to stop.): ')
    if name == '':
        break
    cat_names = cat_names + [name] # List concatenation
print('The cat names are:')
for name in cat_names:
    print(name)
