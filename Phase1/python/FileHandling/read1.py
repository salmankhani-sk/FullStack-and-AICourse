with open("pract2.txt", "r") as file:
    lines = file.readlines()
    for i in lines:
        print(i.strip())  