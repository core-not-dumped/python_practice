# set = collection which is unordered, unindexed

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup"}


utensils.add("napkin")
utensils.remove("fork")
# utensils.clear()
# utensils.update(dishes) # utensils = utensils + dishes
dinner_table = utensils.union(dishes)

print(utensils.difference(dishes))
print(utensils.intersection(dishes))

for x in utensils:
    print(x)




