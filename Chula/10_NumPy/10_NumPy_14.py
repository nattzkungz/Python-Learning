import numpy as np

def sum_2_rows(M):
    return M[::2] + M[1::2]

def sum_left_right(M):
    return M[:,M.shape[1]//2:] + M[:,:M.shape[1]//2]

def sum_upper_lower(M):
    return M[M.shape[0]//2::2] + M[:M.shape[0]//2:2]

def sum_4_quadrants(M):
    return M[M.shape[0]//2::2, :M.shape[1]//2:2] + M[:M.shape[0]//2:2, M.shape[1]::2]

def