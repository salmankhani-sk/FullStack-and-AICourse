with open("urooj.txt","r+") as file:
    file.write("This is a new file created for testing\n")
    file.seek(6)
    print(file.read())