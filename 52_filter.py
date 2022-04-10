# filter() = creates a collection of elements from an iterable for which a function returns
# filter(function, iterable)

friends = [("R", 19),
           ("M", 18),
           ("P", 17),
           ("J", 16),
           ("C", 21),
           ("Ro", 20)]

age = lambda data:data[1] >= 18

drinking_buddies = list(filter(age, friends))

for i in drinking_buddies:
    print(i)


