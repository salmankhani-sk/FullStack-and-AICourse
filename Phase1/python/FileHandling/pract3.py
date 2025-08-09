with open("tayyaba.txt","w+") as file:
    file.write("This is a new file created for testing\n")
    file.write("It contains some sample text for demonstration\n")
    file.seek(0)  
    print(file.read())  