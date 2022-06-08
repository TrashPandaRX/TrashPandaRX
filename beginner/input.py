#learnin' all bout inputs baby!
import random

#randomly made by me with the inspiration of using .join from a "Medium" tech article on how to master python lang.
'''
babble = input("babble something to me, babe: ")
wabble = input("wabble sometin' else to me babe: ")
quaffle = input("quaffle something for me to lean on: ")

unite = [babble, wabble, quaffle]

sumOfEm = ', '.join(unite)

print (sumOfEm)
'''

#feeling out int() conversion
#THIS WORKS! COOL saves me a line of code instead of having to make a separate line to convert string input to an int
'''
def input_then_fuse ():
    one = int(input("gimme a number: "))
    two = int(input("gimme another number: "))
    print("now check this shit out...BLAM!!!")

    fuse = one*two
    print(fuse)

x = 3
while (x > 0):
    input_then_fuse()
    x -= 1

print("aaaaaaaaaaand...The program is done!")
'''

#more input tests, this time break or continue...depending on what i feel like typing

current_number = 200
while current_number > 0:
    current_number -= 6
    print(current_number * random.randrange(1,21))
