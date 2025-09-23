def findStudentByID(students, stdID):
    for student in students:
        if student == stdID:
            return students[student]
    return -1

print(findStudentByID(
{'std001': {'info': {'name': 'John', 'age': 27, 'sex': 'Male'}, 'gpa' : 3.2},
 'std002': {'info': {'name': 'Marie', 'age': 22, 'sex': 'Female'}, 'gpa' : 3.5},
 'std003': {'info': {'name': 'Peter', 'age': 23, 'sex': 'Male'}, 'gpa' : 3.1}},
'std001'))