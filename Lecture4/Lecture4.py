# Skapa klass med hjälp av .csv fil.
# Vi använder oss av student data från google sheets

# OBS UTAN CSV MODULE

class Student:
    def __init__(self, name, dof, fav_sub, hobby) -> None:
        self.name= name
        self.dof = dof
        self.fav_sub = fav_sub
        self.hobby = hobby

    def __str__(self) -> str:
        return f"{self.name}, {self.dof}, {self.fav_sub}, {self.hobby}\n"

students = []

filePath = "Programmering2-Module2-Lectures\Lecture4\students_data.csv"
with open(filePath, 'r', encoding = 'utf8') as file:
    file.readline()
    for row in file:
        row = row.strip("\n")
        row_list = row.split(",")
        students.append(Student(row_list[0], row_list[1], row_list[2], row_list[3]))

print(*students)

for student in students:
    if "programmering" in student.fav_sub.lower():
        print(student.name, student.fav_sub)
