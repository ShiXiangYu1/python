

course_teachers_map = {}
with open('./teacher.txt') as fin:
    for line in fin:
        line = line[:-1]
        course, teacher =line.split(",")
        course_teachers_map[course] = teacher

print(course_teachers_map)

with open('./input.txt') as fin:
    for line in fin:
        line = line[:-1]
        course, sno,sname,sgrade =line.split(",")
        teacher=course_teachers_map.get(course)
        print(course,teacher,sno,sname,sgrade)