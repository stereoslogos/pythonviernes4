sentinel=100

#while
print("")
print("MENU")
print("1 - Greed")
print("2 - Farewell")
print("0 - Exit")
print("")

while sentinel!=0:
    sentinel=int(input("Type 1, 2 or 0: "))
    if sentinel == 1:
        print("Holla!")
    elif sentinel == 2:
        print("So long!")
    elif sentinel == 0:
        break
    else:
        print("Try 1, 2 or 0!")
else:
    print("Done!")