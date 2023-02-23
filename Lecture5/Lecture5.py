# Skapa klass med hjälp av .csv fil.
# Vi använder oss av student data från google sheets

# OBS UTAN CSV MODULE

class Student:
    def __init__(self, name, dob, fav_sub, hobby) -> None:
        self.name= name
        self.dob = dob
        self.fav_sub = fav_sub
        self.hobby = hobby

    def __str__(self) -> str:
        return f"{self.name}, {self.dob}, {self.fav_sub}, {self.hobby}\n"

students = []

filePath = "Programmering2-Module2-Lectures\Lecture5\students_data.csv"
with open(filePath, 'r', encoding = 'utf8') as file:
    file.readline()
    for row in file:
        row = row.strip("\n")
        row_list = row.split(",")
        students.append(Student(row_list[0], row_list[1], row_list[2], row_list[3]))

for student in students:
    if "svenska" in student.fav_sub.lower():
        print(student.name, student.fav_sub)


# Nu vill vi lägga till en student i CSV filen genom att skriva till den

ny_student = ['Hampus','940104','Svenska','Träna']

from csv import writer
# Öppna filen i ‘append’ läget
with open(filePath, 'a', newline='', encoding = 'utf-8') as file:
    # Skapa ett writer object från csv module
    writer_obj= writer(file)
    # Lägg till din data från listan som sista raden i csv
    writer_obj.writerow(ny_student)

print(*students)