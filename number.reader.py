import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)

 