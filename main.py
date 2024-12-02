size = 9
for i in range(size):
    for j in range(size):
        print("*", end=" ")
    print()
print()
for i in range(size):
    for j in range(size):
        print("*" if i == 0 or i == size - 1 or j == 0 or j == size - 1 else " ", end=" ")
    print()
print()
for i in range(size):
    for j in range(size):
        print("*" if i >= j else " ", end=" ")
    print()
print()
for i in range(size):
    for j in range(size):
        print("*" if i == j or j == 0 or i == size - 1 else " ", end=" ")
    print()
print()
for i in range(size):
    for j in range(size):
        print("*" if i + j >= size else " ", end=" ")
    for j in range(size+1):
        print("*" if i >= j else " ", end=" ")
    print()
print()
for i in range(size):
    for j in range(size):
        print("*" if i + j == size - 1 or i == size - 1 else " ", end=" ")
    for j in range(size-1):
        print("*" if i == j + 1 or i == size - 1 else " ", end=" ")
    print()
print()
for i in range(size):
    for j in range(size -1):
        print("*" if i <= j else " ", end=" ")
    for j in range(size):
        print("*" if i + j <= size - 1 else " ", end=" ")    
    print()
print()
for i in range(size):
    for j in range(size):
        print("*" if i == j or i == 0 else " ", end=" ")
    for j in range(size-1):
        print("*" if i + j == size - 2 or i == 0 else " ", end=" ")    
    print()
print()
