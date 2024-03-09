import multiprocessing as mp
import numpy as np
import time

def random_square(seed):
    np.random.seed(seed) #initialises number generator
    random_num = np.random.randint(0, 10)
    return random_num**2 

def plus_cube(x, y):
    return (x+y)**3

def multi_random_squares_time():
    t0=time.time()
    n_cpu = mp.cpu_count()
    pool = mp.Pool(processes=n_cpu)
    results = [pool.map(random_square, range(10000000))]
    t1=time.time()
    return t1-t0

def parallel_cube(vars):
    n_cpu = mp.cpu_count()
    pool = mp.Pool(processes=n_cpu)
    results=[]
    for i in vars:
        results.append(pool.apply(plus_cube, i))
    return results
    
if __name__=='__main__':
    # print(multi_random_squares_time())
    vars=list(zip(range(100), range(100)))
    print(parallel_cube(vars))