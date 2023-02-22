import csv

# Öppna filen, och läsa in den
def readCSV(path:str) -> dict:
    fruits = {}
    file = csv.reader(open(path, "r", encoding="UTF8"))
    for row in file:
        print(row)
        swe, eng = row
        fruits[swe] = eng
    return fruits


def main() -> None:
    filePath = "Programmering2-Module2-Lectures/Lecture2/fruits.csv"
    fruits = readCSV(filePath)
    # vill printa fruits från dict

    for key in fruits:
        # Skriver ut key= swe och value = eng från dict
        print(key.ljust(10) + fruits[key])
        
main()
