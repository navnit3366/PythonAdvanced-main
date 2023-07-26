students_count = int(input())
students_data = {}

for _ in range(students_count):
    name, grade = [float(x)
                   if i % 2 != 0
                   else x
                   for i, x in enumerate(input().split())]
    if name in students_data:
        students_data[name].append(grade)
    else:
        students_data[name] = [grade]

for s_name, s_grade in students_data.items():
    print(f"{s_name} -> {' '.join([str(format(grade, '.2f' )) for grade in s_grade])} (avg: {(sum(s_grade)/len(s_grade)):.2f})")
