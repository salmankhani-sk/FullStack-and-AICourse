while True:
    name = input("Enter your name: (or 'exit' to quit): ")
    if name.lower() == 'exit':
        break
    with open("aizaz.txt", "a+") as file:
        file.write(name + "\n")
        file.seek(0)
        print(file.read())