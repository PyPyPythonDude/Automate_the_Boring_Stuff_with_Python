def spam():
    global eggs
    eggs = 'spam' #this is the global variable

def bacon():
    eggs = 'bacon' #this is a local variable

def ham():
    print(eggs) #this is the global variable


eggs = 42 #global
spam()
print(eggs)
ham()
