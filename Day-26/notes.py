import pandas

list = [1, 2, 3]
new_list = [n + 1 for n in list]
print(new_list)

name = "Myles"
list = [letter for letter in name]
print(list)

list = [i * 2 for i in range(1, 5)]
print(list)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
cap_names = [name.upper() for name in names if len(name) > 5]
print(cap_names)

import random

students_scores = {student: random.randint(1, 100) for student in names}
print(students_scores)

passed_students = {student: score for (student, score) in students_scores.items() if score >= 60}
print(passed_students, '\n')

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

import pandas as pd

data_frame = pd.DataFrame(student_dict)
print(data_frame)
for (index, row) in data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)