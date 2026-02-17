# from existing data
import numpy as np
np.array([1,2,3])
# create a numpy array with empty values 0s
empty=np.zeros(5)
print(empty)

# create a numpy array with value as 1 for 10 elements
one=np.ones(10)
print(one)

print(type(one))
# create evenly spaces values (like range)
arrage_numpy=np.arange(0,20,2)
print(arrage_numpy)

# evenly spaced values
# linspace :linearly spaced numbers -->  it generates evenly spcaed numbers between a string


linear_np=np.linspace(0,1,5)

print(linear_np)
# means:
# start=0
# stop=1

# total number =5
# include both 0 and 1

# step =(stop-start)/(num-1)=(1-0)/(5-1)=1/4=0.25
# step                  value




