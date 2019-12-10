from random import randrange
from random import sample


array = sample(range(0, 100), 50)
array.sort()
searched_value = randrange(0, 100)
print(array)
print(f"Szukana wartosc: {searched_value}")
start = 0
end = len(array)

def bin_search(s, e):
    if s < e:
        if array[s] == searched_value:
            return s
        middle = (s + e) // 2
        if arrat[middle] < searched_value:
            bin_search(middle + 1, e)
        else:
            bin_search(s, middle)
    else:
        bin_search(s, middle)

while start < end:
    middle = (start + end) // 2
    if array[middle] < searched_value:
        start = middle + 1
    else:
        print("Nie ma w liscie tej wartosci")
