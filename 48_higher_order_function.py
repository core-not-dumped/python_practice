# higher order function =
# 1. accepts a function as an argument
# 2. returns a function

def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func("Hello")
    print(text)

hello(loud)
hello(quiet)


def divisor(x):
    def dividend(y):
        return y / x
    return dividend

# divisor return dividend function
divide = divisor(2)

# using that, divide using dividend function
print(divide(10))


