######### Läsa in från fil: the basics ############

# Att öppna fil
# Vi sparar vägen till filen i en variabel och använden dne istället för hela väg-namnet

filePath = "Programmering2-Module2-Lectures/PythonPoem.txt"
infil = open(filePath, "r")

# läs in en rad från fil

s = infil.readline()
s2 = infil.readline() # Vi fortsätter där vi började


# läsa in specifikt antal tecken
s3 = infil.read(15)


# läsa in hela filen till en lista
list = infil.readlines()
print(list)

# Stäng filen
infil.close()

# Hantera slutet av en fil

infil = open(filePath, "r")
nextLine = infil.readline()
while nextLine != "":
    nextLine = infil.readline()
    print(nextLine)
infil.close()

# Man kan också läsa från fil med for-loop, det föredrar vi, då slipper vi stänga filen efteråt!
with open(filePath, "r", encoding="UTF-8") as file:
    for line in file:
        print(line)

######### skriva ut in på fil ############

utfil = open("ny.txt", "w")
utfil.write("Hej :D")
utfil.write("Hej då! :(")
utfil.close()





