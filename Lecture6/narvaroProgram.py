# Att skapa klass mha en CSV fil som vi läser ifrån och skriver till

# Vi skriver ett program som hjälper os att ta närvaro
from datetime import date
from csv import writer

class Student:
    def __init__(self, name, date = date.today(), attendance = "No information") -> None:
        self.name = name
        self.date = date
        self.attendance = attendance

    def __str__(self) -> str:
        return f"{self.name.ljust(30)} {self.date} {self.attendance}"
    
    def setAttendance(self, bool:bool) -> None:
        if self.attendance is not bool:
            if bool:
                self.attendance = True
            else:
                self.attendance = False



def makeStudents(path:str)-> None:
    students = []
    with open(path, 'r', encoding = 'utf-8') as file:
        file.readline()
        for row in file:
            row = row.strip("\n")
            row_list = row.split(",")
            students.append(Student(row_list[0]))
    file.close()
    return students


def attendance(student) -> None:
    answer = input(f"{student.name} (+/-): ")
    if answer == "+" or answer == "-":
        if answer == "+":
            student.setAttendance(True)
        elif answer == "-":
            student.setAttendance(False)
    else:
        print("Use only + or -!")
        answer = input(f"{student.name} (+/-): ")
        attendance(student)


def printStudents(list):
    for student in list:
        print(student)
        

def writeCSV(path, student):
    with open(path, 'a', encoding = 'utf-8', newline ='') as klasslista:
        writerObj = writer(klasslista)
        studentInfo = [student,None,None]
        writerObj.writerow(studentInfo)
    klasslista.close()
            

def main() -> None:
    
    filePath = "Programmering2-Module2-Lectures\Lecture6\klasslista.csv"
    students = makeStudents(filePath)

    print("Välkommen till Te21-Klass-hanterar-programmet")

    while True:
        print("Skriv exit för att avsluta")
        answer = input("Vad vill du göra?\n1. Visa klasslista.\n2. Ta närvaro\n3. Lägg till student\n4. Ändra närvaro\nSvar: ")
        if answer == "1":
            printStudents(students)

        elif answer == "2":
            for student in students:
                attendance(student)
       
        elif answer == "3":
            input_name = input("Efternamn Förnamn: ")
            writeCSV(filePath, input_name)
            students = makeStudents(filePath)

        elif answer == "4":
            input_name = input("Namnet på den du vill ändra närvaro på: ")
            for student in students:
                if input_name in student.name:
                    attendance(student)

        elif answer=='exit':
            break
                    
main()