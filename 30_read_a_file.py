try:
    with open('30_test.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found :(")

