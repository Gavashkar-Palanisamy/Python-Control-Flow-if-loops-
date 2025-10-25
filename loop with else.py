numbers = [2, 4, 6, 8, 10]
n = int(input("Enter n : "))

for i in numbers:
    if i == n:
        print("Number found!")
        break
else:
    print("Number not found in list.")
