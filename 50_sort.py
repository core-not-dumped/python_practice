# sort() method = used with lists
# sort() function = used with iterables

students = ["Squidward", "Sandy", "Patrick", "Spongebob", "Mr.Krabs"]

# students.sort(reverse = True)
# for i in studetns:
#     print(i)

sorted_students = sorted(students, reverse = True)

for i in sorted_studetns:
    print(i)

students = [("Lee", "F", 60),
            ("Park", "A", 33),
            ("Kim", "D", 36),
            ("Choi", "B", 20),
            ("Jung", "C", 78)]

# sorted second argument
grade = lambda grades:grades[1]
students.sort(key = grade, reverse = True)
sorted_students = sorted(students,key=grade)

for i in students:
    print(i)

for i in sorted_studetns:
    print(i)


