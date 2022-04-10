temp = int(input("what is the temperatrue outside?: "))

if not(temp >= 0 and temp <= 30):
    print("the temperature is good today!")
    print("go outside!")
elif not(temp < 0 or temp > 30):
    print("the temperature is bad today!")
    print("stay inside!")

