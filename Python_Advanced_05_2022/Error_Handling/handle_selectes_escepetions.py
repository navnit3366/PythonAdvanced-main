while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Ooops i want a number")
        