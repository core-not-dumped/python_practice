# dictionary = A changeable, unordered collection of unique key:value pair
# use hasing so it is very fast


capitals = {'USA':'Washington DC',
            'India':'New Dehli',
            'China':'Beijing',
            'Russia':'Moscow'}

# print(capitals['Germany'])    # error
print(capitals.get('Germany'))  # safer


capitals.update({'Germany':'Berlin'})
capitals.update({'USA':'Las Vegas'})    # new capital
capitals.pop('China')
# capitals.clear()

print(capitals.keys())
print(capitals.values())
print(capitals.items())     # entire information

for key,value in capitals.items():
    print(key, value)


