rows = int(input("How big would you like your pyramid? "))

for row in range(rows):
    for col in range(row + 1):
        print('*', end=" ")
    print()