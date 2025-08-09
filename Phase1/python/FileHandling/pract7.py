entry = input("write ka khpal nan activity: ")
with open("activity.txt", "a+") as file:
    file.write(entry + "\n")
    file.seek(0)
    print("Activity log:")
    print(file.read())
    