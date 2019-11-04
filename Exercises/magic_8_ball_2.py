import random

# Create a list to store the messages
messages = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']

# Display a random message from the list above.
print(messages[random.randint(0, len(messages) - 1)])
