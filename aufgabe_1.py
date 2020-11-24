# Carina Moitov
# Arthur Flaum
# Florian Ewald, 333 068 94
import random

def printMatrix(M):
    for m in M:
        print("["+",\t".join(map(str, m))+"]")
    print()

def is_integer_matrix(M):
    k = len(M[0])
    for m in M:
        if len(m) != k:
            return False
        for n in m:
            if int(n) != n:
                return False
    return True

def generate_matrix(k, l, i, j):
    if (k <= 0) or (l <= 0):
        print("k and l have to be positive integer!")
        return
    M = []
    for m in range(k):
        M.append([])
        # for n in range(l):
        #     M[m].append(random.randint(i, j))
        M[m] = [random.randint(i, j) for n in range(l)]

    return M

def multiply_matrix(k, l, i, j):
    M = generate_matrix(k, l, i, j)
    N = generate_matrix(l, k, i, j)
    # (lxm) x (mxn) = lxn
    # -> (kxl) x (lxk) = (kxk) 
    P = []
    print("Matrix M ({}, {}):".format(k, l))
    printMatrix(M)
    print("Matrix N ({}, {}):".format(l, k))
    printMatrix(N)
    for m in range(k):
        P.append([])
        for n in range(k):
            tmp = 0
            for o in range(l):
                tmp += M[m][o]*N[o][n]
            P[m].append(tmp)
    return P

# Task 1a
print("Überprüfung der Funktion is_integer_matrix")
M = [[10, 3, 29, 4],[4, 77, 191, 2],[85, 9, 2, 37]]
printMatrix(M)
print(is_integer_matrix(M))

M = [[13, 3.75],[4.0, 2.23],[80, 3]]
printMatrix(M)
print(is_integer_matrix(M))

M = [[13, 3],[4],[80, 3]]
printMatrix(M)
print(is_integer_matrix(M))

# Task 1b
print("Überprüfung der Funktion generate_matrix")
M = generate_matrix(3,4, 1,10)
printMatrix(M)
print(is_integer_matrix(M))

P = multiply_matrix(2, 3, 1, 5)
print("Calculated matrix P: ")
printMatrix(P)

k = int( input("Please enter an integer for k:\n") )
l = int( input("Please enter an integer for l:\n") )
i = int( input("Please enter an integer for i:\n") )
j = int( input("Please enter an integer for j:\n") )

P = multiply_matrix(k, l, i, j)
print("Calculated matrix P: ")
printMatrix(P)
