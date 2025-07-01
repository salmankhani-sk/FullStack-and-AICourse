try:
    with open("data.txt", "w") as file:
        file.write("This is our data file")
        
except FileNotFoundError:
    print("Da file mung sara nishta")