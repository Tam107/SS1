def searchForStudent(students, key, value):
    result = []
    for std_id, data in students.items():
        if key in data.get('info', {}):
            if data['info'][key] == value:
                result.append(std_id)
        # elif key in data:
        #     if data[key] == value:
        #         result.append(std_id)
    return result if result else -1


students = {
    'std001': {'info': {'name': 'John', 'age': 27, 'sex': 'Male'}, 'gpa': 3.2},
    'std002': {'info': {'name': 'Marie', 'age': 22, 'sex': 'Female'}, 'gpa': 3.5},
    'std003': {'info': {'name': 'Peter', 'age': 23, 'sex': 'Male'}, 'gpa': 3.1}
}

print(searchForStudent(students, 'name', 'John'))   # ['std001']
print(searchForStudent(students, 'sex', 'Male'))    # ['std001', 'std003']
print(searchForStudent(students, 'age', 50))        # -1
print(searchForStudent(students, 'gpa', 3.5))       # ['std002']