# Hur lägger vi till till en existerande CSV fil?

ny_student = ['Arda','051025','Engelska/Programmering','gott och blandat']

from csv import writer
# Öppna filen i ‘append’ läget
with open('Programmering2-Module2-Lectures\Lecture5\students.csv', 'a', newline='') as file:
    # Skapa ett writer object från csv module
    writer_obj= writer(file)
    # Lägg till din data från listan som sista raden i csv
    writer_obj.writerow(ny_student)