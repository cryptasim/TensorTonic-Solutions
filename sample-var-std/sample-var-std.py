import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    x = np.asarray(x, dtype=float)
    m = np.mean(x)
    s = 0.0
    for _ in x:
        s += (_ - m)**2
    v = s / (len(x) - 1)
    sd = v**0.5
    return {"variance": float(v), "standard_deviation": float(sd)}
    pass