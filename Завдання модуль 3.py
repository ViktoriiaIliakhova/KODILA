# Task 1
product_dictionary = {
    "bakery": ["bread", "donuts", "buns."],
    "grocery_store": ["carrot", "celery", "arugula."]
}
for key, value in product_dictionary.items():
    print(f"I am going to {key.capitalize()} and buy there "
          f"{value [0].capitalize()}, {value [1].capitalize()}, {value [2].capitalize()}")
total_amount = len(product_dictionary["bakery"] + product_dictionary["grocery_store"])
print("I buy", total_amount, "products in general.")

# Task 2
for number in range(0, 100):
    if number % 5 == 0:
        print(number ** 3)
