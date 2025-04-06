str = "Python is love"
#love is python
a = str.split()
print(a)
b = a[::-1].join(a)
print(b)
c = " ".join(b)
print(c)

# print(" ".join(a[::-1]))
