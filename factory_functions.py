

#Brioche Factory TDD
#Our factory knows inputs and outputs

## Make bread
#Inputs would be water, flour, eggs,
#Outputs would be dough

# Bake
def make_bread(arg1, arg2, arg3):
    list = []
    list.append(arg1)
    list.append(arg2)
    list.append(arg3)
    for item in list:
        if item == 'water':
            list.(item)
        elif item == 'flour':
            list.pop(item)
        elif item == 'eggs':
            list.pop(item)

    if len(list) == 0:
        return 'dough'
    else:
        return 'not dough'

def bake(arg1):
    if arg1 == 'dough':
        return 'brioche'
    else:
        return 'not brioche'

def run_factory(arg1, arg2, arg3):
    pass
