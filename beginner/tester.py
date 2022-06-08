num_range = []
x = 0   #incrementing this and inserting it into num_range each iteration

while 10 not in num_range:
    num_range.append(x)
    x = x+1

#numbers = ", ".join(str(num_range))        *Ended up being unnecessary complexity AND wrong
print(num_range)