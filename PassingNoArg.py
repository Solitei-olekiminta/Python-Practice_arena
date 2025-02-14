def make_pizza(*toppings):
    """"Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('Pepperoni')
make_pizza('Mushrooms', 'green peppers', 'extra cheese')
