# Man kan även läsa igenom hela filen med en for slinga

with open("Programmering2-Module2-Lectures\Lecture1\PythonPoem.txt", "r", encoding= "utf8") as file:
    for line in file:
        print(line)

