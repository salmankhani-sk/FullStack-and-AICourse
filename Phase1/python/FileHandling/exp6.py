with open("alam.txt","w+") as file:
    file.write("I am ihtesham Alam.\n")
    file.seek(0)
    print(file.read())