import timeit
def my_function():
    y = 3.1415
    for x in range(100):
        y = y ** 0.7
    return y

print(timeit.timeit(my_function, number=100000))