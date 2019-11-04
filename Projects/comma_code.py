'''
This program contains a function that takes a list value as an argument
and returns a string with all items separated by a comma and a space,
with the word 'and' inserted before the last item.
'''

def func(some_list):
    if len(some_list) == 0:
        return ''
    elif len(some_list) == 1:
        return some_list[0]
    else:
        part_1 = ', '.join(some_list[:-1])
        part_2 = ' and ' + some_list[-1]
    return part_1 + part_2

spam = ['cats', 'spam', 'eggs', 'bananas', 'tofu']
print(func(spam))
