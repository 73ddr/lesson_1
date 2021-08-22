a_list = input("Введите любые положительные числа" )

print(a_list)
new_list = a_list.split()
for i in range(0, len(new_list)-1, 2):
    new_list[i], new_list[i + 1] = new_list[i + 1], new_list[i]
    print(new_list)


















