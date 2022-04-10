# **kwargs = parameter that will pack all arguments into a dictionary
# useful so that a function can accept a varying amoount of keyword arguments


def hello(**kwargs):
    print("Hello " + kwargs['first'] + " " + kwargs['last'])
    for key, value in kwargs.items():
        print(value)


hello(first="Bro", middle="Dude", last="Code")


