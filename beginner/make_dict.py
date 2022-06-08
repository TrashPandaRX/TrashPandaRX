users = []      #this is a list, not a dictionary. remember they have {} and require key,value pairs

def input_name():
    keep_going = True
    while (keep_going == True):
        name = input("Please input a name or 'quit'/'done' if you dont want to add more: ")
        
        if name == 'quit' or name == 'done':
            break              #exit while loop if name == 'quit' or 'done'
        
        users.append(name)


input_name()
print(", ".join(users))

'''
okay my setup for this lil program:

-make an empty list to put names into
-add names until user types done/quit
-add commas between each element of the list 'users' utilizing  .join()
-print list of names out
-end program

'''