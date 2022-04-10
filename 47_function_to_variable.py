def hello():
    print("Hello")

print(hello)
hi = hello
print(hi)

# hello and hi is same function
# same memory address
hi()

say = print
say("Whoa! I can't believe this work! :)")


