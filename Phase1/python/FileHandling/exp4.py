with open("data.txt","w+") as file:
    file.write("This is a new file.\n")
    file.seek(0)
    print(file.read())