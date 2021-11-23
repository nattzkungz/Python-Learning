import numpy as np

def get_column_from_bottom_to_top(A, c):
    return A[:,c,][::-1]

def get_odd_rows(A):
    return A[1::2]

def get_even_column_last_row(A):
    return A[-1, ::2]

def get_diagonal1(A):
    a = np.array([A[e,e] for e in range(len(A))])
    return a

def get_diagonal2(A):
    a = np.array([A[e,-e-1] for e in range(len(A))])
    return a

exec(input().strip())