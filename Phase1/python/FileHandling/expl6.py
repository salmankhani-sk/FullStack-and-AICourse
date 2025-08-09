with open("raja.txt",'a+') as file:
    file.write("Salman Khan\n")
    file.seek(5)
    print(file.read())
    