# Introduktion till filhantering

# Att kunna läsa in från en fil underlättar i programmeringen
# speciellt om man handskas med långa strängar eller mycket data

# Här är en funktion som läser in från en fil
def read_file(filename) -> list[any]:
    file = open(filename, "r")                  # öppna filen för läsning, r = read
    #first_row = file.readline()                # läser in en rad i filen
    list = file.readlines()                     # läser in alla rader i filen
    
    file.close()                                # stänger filen
    print("The file was read successfully")
    return list                                 # funktionen returnerar listan med alla inlästa rader                     

# Filer är ett bra sätt att spara data mellan programkörningar
# Den här funktionen skriver till en fil:
def write_to_file(new_file_name, info):
    out_file = open(new_file_name,"w")              # öppna en fil för w = write
    #out_file.write(info)                            # Skriver ut en rad
    out_file.writelines(info)                       # Skriver ut en lista

    out_file.close()                                # Stänger filen
    print("The info is saved in: " + new_file_name)


def main():
    string_list = read_file("Programmering2-Module2-Lectures\Lecture1\PythonPoem.txt")
    string = ""
    for item in string_list:
        item.split("\n")
        string+= item

    write_to_file("save1.txt", string)

main()