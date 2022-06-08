array = [0] *10

print(array[5])

array[5] = 2 # 6th item in array

print(array[5])
print("testing something else:\n")

for each in array:      # wow apparently the temp variable "each" isnt a numerical value, rather it is a reference to the current indicie of the array/list
    {
        print(each)
    }