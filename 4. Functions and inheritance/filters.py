grades = ["A", "B", "F", "D", "F", "C"]


def remove_fails(grade):
    return grade != "F"


filtered_grades = []
for grade in grades:
    # filtered_grades.append(remove_fails(grade)) doesn't work?
    if grade != "F":
        filtered_grades.append(grade)
print(filtered_grades)


# using filter (testing_function, data)

print(list(filter(remove_fails, grades)))


# using comprehension
# print([remove_fails(grade) for grade in grades]) doesn't work?

print([grade for grade in grades if grade != "F"])
