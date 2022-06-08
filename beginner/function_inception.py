'''
test to see if you can put functions as arguments for other functions...
also trying to guess how to return values the former point seems quite
likely possible. the latter...i might as well just google it tbh...
'''

def test(int_y):
    print(f"{int_y}")

def return_num (x = 0):
    return x

test(return_num(input("insert an integer (ps if you remove this 'input function' it will default to 0) ", )))

'''
works like a charm! Basically if you leave the argument part
of return_num empty, it will use the default value for x (eg 0),
OTHERWISE if you pass an argument into return_num, then test()
will instead print that value out.

PS i did the return thing right :D

PPS if you care to know...i intended the return_num to only accept integer values...
but at present idk how to sanitize my input to do so. Well that isnt to say idk HOW,
I can definitely cook something up. i just wonder if its the industry standard means
of accomplishng that goal.
'''
