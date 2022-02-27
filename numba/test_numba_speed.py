# Reference: https://numba.readthedocs.io/en/stable/user/5minguide.html, https://numba.readthedocs.io/en/stable/user/performance-tips.html#performance-tips

# %%
from timeit import timeit
from numba import jit
import numpy as np

# %%
x = np.arange(100).reshape(10, 10)

def go_fast(a):
    trace = 0.0
    for i in range(a.shape[0]):
        trace += np.tanh(a[i, i])
    return a + trace

print(go_fast(x))

#%%
@jit(nopython=True) # Set "nopython" mode for best performance, equivalent to @njit
def go_fast_numba(a): # Function is compiled to machine code when called the first time
    trace = 0.0
    for i in range(a.shape[0]):   # Numba likes loops
        trace += np.tanh(a[i, i]) # Numba likes NumPy functions
    return a + trace              # Numba likes NumPy broadcasting

print(go_fast_numba(x))

# %%
%%timeit
go_fast(x)

# %% 10x faster than above function
%%timeit
go_fast_numba(x)

# %%
@jit # is numba decorator
# compilation mode is to essentially compile the decorated function so that it will run entirely without the involvement of the Python interpreter
@jit(nopython=True)
# object mode
# Note that Pandas is not understood by Numba and as a result Numba would simply run this code via the interpreter but with the added cost of the Numba internal overheads!
@jit