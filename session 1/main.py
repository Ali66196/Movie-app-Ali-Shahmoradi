import math

st = [
    {"id": 1, "name": "Alice", "score": 3},
    {"id": 2, "name": "Bob", "score": 7.87},
    {"id": 3, "name": "Charlie", "score": 9.001},
    {"id": 4, "name": "David", "score": 11},
    {"id": 5, "name": "Eve", "score": 13},
    {"id": 6, "name": "Frank", "score": 8},
    {"id": 7, "name": "Grace", "score": 9},
    {"id": 8, "name": "Hannah", "score": 9.2},
    {"id": 9, "name": "Isaac", "score": 8.86}
]

def nomre_prss(st):
    prss_student = []
    for student in st:
        ceil = math.ceil(student["score"])
        student["score"] = ceil
        student["passed"] = ceil >= 10
        prss_student.append(student)
    return prss_student

prss_student = nomre_prss(st)

print("Passed Student:")
for student in prss_student:
    if student["passed"]:
        print(student["name"],student["score"])
print("Fail Student:")
for student in prss_student:
    if not student["passed"]:
        print(student["name"],student["score"])




        