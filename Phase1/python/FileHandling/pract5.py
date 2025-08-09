with open("prob1.txt","a+") as file:
    file.write("John the don\n")
    file.seek(0)
    print(file.read())