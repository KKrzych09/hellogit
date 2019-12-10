a = int(input("Wprowadz a:"))
b = int(input("Wprowadz b:"))
c = int(input("Wprowadz c:"))

if a == 0:
    if b == 0:
        if c == 0:
            print("Nieskończenie wiele rozwiązań.")
        else:
            print("Brak rozwiązań.")
    else:
        print(f"x0 = {-c / b}")
else:
    delta = (b ** 2) - (4 * a * c)
    if delta == 0:
        x = -b / (2 * a)
        print(f"x0 = {x}")
    elif delta > 0:
        x1 = (-b - delta ** (1/2)) / (2 * a)
        x2 = (-b + delta ** (1/2)) / (2 * a)
        print(f"x1 = {x1}, x2 = {x2}")
    else:
        print("Nie ma miejsc zerowych.")