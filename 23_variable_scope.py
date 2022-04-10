# scope = The region that a variable is recognized
# A varaiable is only available from inside the region it is created
# A global and locally scoped versions of a variable can be created

name = "Bro" # global scope

def display_name():
    name = "Code" # local scope
    print(name)


print(name)
display_name()

