L = [23, 42, 60, 10, 54, 73]
for i in range(0, 5):
    print(i, L[i])

Marks = [45, 34, 67, 70]
for j in range(len(Marks)):
    Marks[j] = Marks[j] + 5
print(Marks)

def linsearch(lst, target):
    for j in range(len(lst)):
        if(lst[j] == target):
            return j
    return -1  # Return -1 if the target is not found

L = [23, 42, 60, 10, 70, 50]
found = linsearch(L, 10)
print('location =', found)

def largest(A):
    large = A[0]
    for j in range(len(A)):
        if A[j] > large:
            large = A[j]
    return large

L = [23, 42, 60, 10, 70, 50]
found_large = largest(L)
print('largest element =', found_large)

l1=[1,4,5]
l2=[3,7,9]
l3=l1+l2
print(l3)

L3=[1,14,8,6,9]
L3.sort()
print(L3)

b=[0]*4
print(b)

def make_l(length):
    return [None] * length

A = make_l(8)
for i in range(8):
    A[i] = input("Enter value: ")

print("A =", A)


