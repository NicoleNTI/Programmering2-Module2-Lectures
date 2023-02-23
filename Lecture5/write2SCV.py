# Hur skriver vi till en CSV fil?

import csv
# öppna filen i ‘w’ läget:
file = open('Programmering2-Module2-Lectures\Lecture5\Test.csv', 'w')

# skapa ett csv writer objekt
writer_obj = csv.writer(file)

# skriv en rad till csv filen
writer_obj.writerow()

# stäng filen
file.close()




# With statement
from csv import writer

header = ['name', 'birthday', 'fav_sub', 'hobby']
data = ['Nicole', '990426', 'Web-programming', 'games']

with open('Programmering2-Module2-Lectures\Lecture5\student.csv', 'w', encoding='UTF8') as file:
    writer = csv.writer(file)

    # write the header
    writer.writerow(header)

    # write the data
    writer.writerow(data)




# Flera rader data:
from csv import writer

header = ['name', 'birthday', 'fav_sub', 'hobby']
data = [
    ['Nicole', '990426', 'web-programming', 'games'],
    ['Eddie', '050809', 'Programmering', 'Programmering'],
    ['Rasmus', '051003', 'prog2', 'magic the gathering'],
    ['Diana', '030824', 'Fysik, Matte', 'Träna'],
    ['Omar', '050908', 'ENG', 'Sova']
]

with open('students.csv', 'w', encoding='UTF8', newline='') as file:
    writer = csv.writer(file)

    # skriver ut titlarna
    writer.writerow(header)

    # skriver alla rader till filen!
    writer.writerows(data)

