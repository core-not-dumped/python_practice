# str.format() = optional method that gives users

animal = "cow"
item = "moon"

print("The " + animal + " jumped over the " + item)
print("The {} jumped over the {}".format(animal,item))
print("The {1} jumped over the {0}".format(animal,item)) # positional argument
print("The {animal} jumped over the {item}".format(animal = "cow",item = "moon")) # keyword argument
print(f"The {animal} jumped over the {item}") # important ********


text = "The {} jumped over the {}"
print(text.format(animal,item))

name = "Bro"
print("Hello, my name is {}".format(name))
print("Hello, my name is {:10}. Nice to meet you".format(name)) # add padding
print("Hello, my name is {:<10}. Nice to meet you".format(name)) # left align
print("Hello, my name is {:>10}. Nice to meet you".format(name)) # right align
print("Hello, my name is {:^10}. Nice to meet you".format(name)) # center align

num = 1000
print("The number is {:.2f}".format(num))
print("The number is {:,}".format(num))      # add ,
print("The number is {:b}".format(num))      # binary expression
print("The number is {:o}".format(num))      # 8
print("The number is {:X}".format(num))      # 16
print("The number is {:E}".format(num))      # scientific


