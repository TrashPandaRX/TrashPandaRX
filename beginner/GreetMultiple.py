def greet_usrs(names):
    '''Print a simple greeting to each user in the list.'''
    for name in names:
        msg = f"Hello there, {name.title()}!"
        print (msg)

usrs = ["ally","barry","cooch"]
greet_usrs(usrs)
    
