A, B = input().split()
A_err = int(A[::-1])
B_err = int(B[::-1])

if A_err > B_err:
    print(A_err)
else:
    print(B_err)