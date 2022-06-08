def create_pizza(size, *toppings):
    print(f"\n Making a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")   '''Btw apparently the contents of {} are classified as a string, so you cant use arithmetic with integers within it, EG {toppings + 1}'''