with open("data.txt", "r+") as file:
    print(file.read())
    file.seek(0)
    file.write("This is a new line.\n")
    file.seek(0)
    print(file.read())