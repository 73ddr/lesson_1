rating = [8, 7, 5, 4, 2, 1]

rating_2 = int(input("Enter rating: "))
inserted = False
for i, elem in enumerate(rating):
    if rating_2 > elem:
        rating.insert(i, rating_2)
        inserted = True
        break

if not inserted:
    rating.append(rating_2)

print(rating)


