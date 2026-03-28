fruits = ["Apple", "Banana", "Mango"]

for index, fruit in enumerate(fruits):
    print(index, fruit)

print("Using start parameter")
text = "PYTHON"

for index, letter in enumerate(text):
    print("Letter:", letter, "Position:", index)
numbers = [12, 7, 18, 5, 20, 9]

for index, num in enumerate(numbers):
    if num % 2 == 0:
        print("Even number", num, "found at index", index)