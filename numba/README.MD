# Numba code optimization
Numba is great for numpy calculation and loop over mathematical operation including nump.linalg as well. However, pandas is not tested yet but 5 minutes guide suggest blended mode(object mode) is utilized when your python code is a combination between pandas and numpy.

```
conda create --name numba_test python=3.7
pip install pandas 
pip install numba
pip install ipykernel
conda activate numba_test
```
I use timeit module as well, if you can't use it. You can directly install the package.

## Interesting thing to try out
1. Test processing data with pandas chaining and pipe to see speed
2. Learn how to modify data processing in pandas to numpy in order to increase speed
3. Learn decorator and other usecase of numba
## Code reference
1. [5 minutes guide](https://numba.readthedocs.io/en/stable/user/5minguide.html)
2. [performance tips](https://numba.readthedocs.io/en/stable/user/performance-tips.html#performance-tips)