while(True):
    a = input("Enter the no:")
    x = [y for y in a]
    sum = 0

    for i in range(len(a)):
        n = int(x[i])
        sum = sum + n**len(a)

    if sum == int(a):
        print(sum,"is an armstrong no!")
    else:
        print("Not an armstrong no.!")