# Loop Control Statements

while True:
    name = input("Enter your name:")
    if name != "":
        break

phone_number = "123-456-789"

for i in phone_number:
    if i == "-":
        continue
    print(i)

for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i)

