word = input("Введите несколько слов разделяя одним пробелом").split( )
for num, elem in enumerate(word, 1):
    print(f"#{num}-{elem[:10]}")



