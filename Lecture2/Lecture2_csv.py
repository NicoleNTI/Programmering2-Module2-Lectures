# Att öppna en CSV fil
# Vi öppnar och läser in raderna i CSV-filen, och sen skriver ut varje rad utan "enter" = \n
with open("Programmering2-Module2-Lectures/Lecture2/fruits.csv","r",encoding="UTF-8") as csv_file:
    for line in csv_file:
        line = line.strip("\n")
        list = line.split(",")
        print(*list)