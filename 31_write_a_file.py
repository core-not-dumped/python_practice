text = "Yoooooooooooo\nThis is some text\n"

with open('31_test.txt', 'w') as file:
    file.write(text) # rewrite


text = "abc"

with open('31_test.txt', 'a') as file:
    file.write(text)

