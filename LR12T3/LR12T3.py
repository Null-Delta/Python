command = input()

arguments = command.split()

if arguments[0] == "cat":
    files = arguments[1::]
    for file in files:
        try:
            openedFile = open("LR12T3/" + file, "r")
            print(openedFile.read())
            openedFile.close()
        except:
            print("Error in file reading")
else:
    print("Wrong command")