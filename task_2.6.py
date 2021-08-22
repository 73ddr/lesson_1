products = []
counter = 1
command = " "
while command != "stop":
    name = input("name")
    price = input("price")
    amount = input("amount")
    units = input("units")
    products.append(
        counter, {"name": name, "price": price, "amount": amount, "units": units})

    counter += 1
    command = input("Write "stop" for stop inputting:")

result_lict = {}
for numb, prod_dict in products:
    for key, value in prod_dict.items():
        if not result_lict.get(key):
            result_list[key] = [value]
        else:
            result_list[key].append(value)

print(result_lict)
