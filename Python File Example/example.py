file = open("file.txt", "w+")

print(file.name, "closed:", file.closed)
print("Access mode:", file.mode)

file.close()

print(file.name, "closed:", file.closed)