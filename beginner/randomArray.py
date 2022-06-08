#random array
'''
    okay so before i had "randomArr[element] = min(random()*5)" because i thought
    that it would simply stuff the "min()" part into that indicie of the array...
    apparently that is wrong "element" is NOT a temp numerical value, its literally
    a reference to the indicie. so you cant use element to return the loop number its at.
    by this i mean on loop[] 0 of like 10, element != 0. but rather whatever is at loop[0]
    which could be 'toad toes' or 'hubba lubba rub rub'

    wrong again i tried "element = min(random()*5)" and instead of getting a syntax error,
    i got an error saying element:int or element:float ???

    code pre fix

    *
    from random import seed
    from random import random

    seed(1)

    print (random())

    randomArr = [0] * 10
    for element in randomArr:
        {
            element = min(random()*5)
        }
    print (randomArr)
    *

    see https://stackoverflow.com/questions/54974579/change-values-in-a-list-using-a-for-loop-python
        https://stackoverflow.com/questions/14785495/how-to-change-index-of-a-for-loop


OKAY SO APPARENTLY YOU ARENT ALLOWED TO MODIFY SHIT DURING A FOR LOOP BECAUSE ITS ITERABLE
so instead what you would want to do is make a "List Comprehension"
https://stackoverflow.com/questions/4081217/how-to-modify-list-entries-during-for-loop/4082739

a = [1, 3, 5]
b = a
a[:] = [x + 2 for x in a]
print(b)

'''

from random import seed
from random import random

seed(1)
x = 0
goonie = 'goonie'

randomArr0 = None       #just testing to see how you basically DECLARE a variable without implementing it
randomArr1 = [0] * 10
randomArr2 = randomArr1
print (randomArr2)

# "print (random())" just to check if random() works

for element in range (0,10):
    {
        print(element)
    }

print('\n')     #make space

for letter in goonie:
    {
        print(letter)
    }

randomArr1[:] = [ x+1 for x in randomArr1]    #ps you cant just say x = 5 or some shit. only arithmetic operators

print (randomArr2)      #randomArr2 is a reference to the address of randomArr1
print (randomArr1)

randomArr1 = [0]*10

print (randomArr1)

randomArr1[:] = [ (x+random())*5 for x in randomArr1]

print (randomArr1)
print (randomArr2)      #not sure why randomArr2 is still saying the results of the first for looped x+1 randomArr1

randomArr3 = [0] * 50
randomArr3 = [ x**3 for x in range(1000, 1, -5)]
print (randomArr3)