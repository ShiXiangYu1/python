
# key :course,value:grade list
course_grades={}

with open("input.txt") as fin:
    for line in fin:
        line=line[:-1]
        course,son,sname,grade=line.split(",")
        if course not in course_grades:
            course_grades[course]=[]
        course_grades[course].append(int(grade))

print(course_grades)

for course,grades in course_grades.items():
    print(course,max(grades),min(grades),sum(grades)/len(grades))