A = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print("Before Sorting:", A)

i = 0
while(i < 9):  # Outer loop, iterates through the entire list
    j = i + 1
    while(j < 10):  # Inner loop, compares the current element with the next one
        if(A[i] > A[j]):  # If current element is greater, swap
            print("Swapping", A[i], A[j])
            t = A[i]  # Swap A[i] and A[j]
            A[i] = A[j]
            A[j] = t
        j = j + 1
    i = i + 1

print("After Sorting:", A)
