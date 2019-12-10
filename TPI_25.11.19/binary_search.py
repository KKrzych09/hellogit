from random import randrange
from random import sample


array = sample(range(0, 100), 50)
array.sort()
searched_value = randrange(0, 100)
print(array)
print(f"Szukana wartosc: {searched_value}")
start = 0
end = len(array)

while start < end:
    middle = (start + end) // 2
    
    if array[middle] < searched_value:
        start = middle + 1
    else:
        end = middle

if array[start] == searched_value:
    print(f"Szukana wartosc jest na pozycji: {start + 1}")
else:
    print("Nie ma w liscie tej wartosci")
