a_counter = 0
filnamn = "Programmering2-Module2-Lectures/Lecture1/PythonPoem.txt"
infil = open(filnamn,"r", encoding="utf8")
for rad in infil:
    for bokstav in rad:
        if bokstav == "a":
            a_counter += 1

print(f"This many letter a's in PythonPoem.txt: {a_counter}")