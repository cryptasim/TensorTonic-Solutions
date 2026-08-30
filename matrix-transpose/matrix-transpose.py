import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    m = len(A)
    n = len(A[0])
    B = np.empty((n,m), dtype=np.array(A).dtype)
    for i in range(n):
        for j in range(m):
            B[i][j] = A[j][i]
    return B
    pass
