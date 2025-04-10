#Take target value from user to find sum of any two nos in the list for the target value
n = int(input("Enter the target value: "))
a = [0,1,2,3,4,5,6,7,8,9]
def tar_add(n,a):
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i] + a[j] == n:
                print(a[i], a[j])
tar_add()