name = input("Enter name: ")

match name:
    case "Harry" | "Hermione" | "Ron": # | is basically or inside "match" function
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _: # means whatever case isn't listed above
        print("Who?")
