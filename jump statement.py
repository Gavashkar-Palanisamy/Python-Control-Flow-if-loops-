# Break Example
print("Break Example:")
for i in range(5):
    if i == 3:
        break  # stops the loop when i == 3
    print(i)

# Continue Example
print("\nContinue Example:")
for i in range(5):
    if i == 4:
        continue  # skips the iteration when i == 4
    print(i)

# Pass Example
print("\nPass Example:")
for i in range(5):
    if i == 2:
        pass  # does nothing, acts as a placeholder
    print(i)
