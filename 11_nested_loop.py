rows = input("How many rows?: ")
columns = input("How many columns?: ")
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")   # \n not printed
    print()



