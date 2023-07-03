# LIST ds, It is ordered and changeable
Cars = ["Mercedes", "Toyota", "Nissan", "Range"]
Cars[1] = "Subaru"
Cars.append("Mitsubishi")
Cars.insert(2, "Bmw")
Cars.pop(0)
Cars.remove("Range")
Cars.reverse()
Cars.sort()
Cars.copy()
print(Cars)

# this is a tuple, it is unchangeable
fruits = ("mangoes", "oranges", "pineapples", "apples", "oranges")
x = fruits.count("oranges")
print(x)

for x in fruits:
    print(x)

# sets Ds, unordered. order changes anytime. it is unchangeable
countries={"kenya", "uganda","Tanzania"}
print(countries)

#dictionaries
class Yellow:
    pass


matunda= {"amount": 40,
          "jina": "Ndizi",
          "rangi": "Yellow",
          "size": "large"}

matunda.pop("amount")
print(matunda)