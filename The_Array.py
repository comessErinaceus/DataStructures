## Fixed length container of n elements usually indexable from the range [0, n-1], sometimes contiguous memory depending on language

## Imports
import random
from matplotlib import pyplot as plt
import numpy as np
import time


## GLOBAL VARS
#spacer = ("#----------###----------#\n")
NUM_ARRAY_DRAWS = random.randint(1 , 6)
RAND_PICKS = []
BIG_ARRAY = []
BIGGER_ARRAY = []

BIG_ARRAY_INSERT_TIMES = []
BIG_ARRAY_SEARCH_TIMES = []

BIG_ARRAY_SIZE = 10000



BIGGER_ARRAY_SIZE = 100000
BIGGER_ARRAY_INSERT_TIMES = []
BIGGER_ARRAY_SEARCH_TIMES = []


## DEFINE py functions
def add_space():
    spacer = ("#----------###----------#\n")
    print(spacer)

def print_arr_rand_index(arr, picks):
    arr_len = int(len(arr)) -1  ## GET ARRAY LEN: array len returns number that starts counting from 1 instead of from 0. will cause index out of bounds

    ## GET INDEX: rand_index is (0 -> arr_len inclusive)
    rand_index = random.randint(0,arr_len)
    

    ## MAKE Mutable ARRAY; new_arr = old_arr makes each point to same mem location
    ### use list, slicing [:], or copy.copy() to make mutable copy of array
    if rand_index not in picks:
        mod_arr = arr[:]
        mod_arr[rand_index] = "["+ str(mod_arr[rand_index]) + "]"
        print("At index: ",rand_index, mod_arr,"Array Address: ",id(mod_arr),"\n")

        picks.append(rand_index)


def time_arr_access(arr, relv_times):
# pick rand index
    index = random.randint(0, len(arr)-1)
    # Start the clock
    start_time = time.time()
    item = arr[index]
    stop_time = time.time()

    # get diff in times
    time_diff = stop_time - start_time

    # record elapsed time to the relevant array
    relv_times.append(time_diff)

def time_arr_insert_replace(arr, relv_times):
# pick rand index
    index = random.randint(0, len(arr))
    # Start the clock
    start_time = time.time()
    arr.insert(index, 5)
    stop_time = time.time()

    # get diff in times
    time_diff = stop_time - start_time

    # record elapsed time to the relevant array
    relv_times.append(time_diff)

def plot_data(data_arr, title):
    #x_values = [0,1,2,3]
    #y_values = [5,6,7,8]

    #plt.plot(x_values, y_values)
    # x = np.linspace(0, 2*np.pi, 200)
    # y = np.sin(x)

    fig, ax = plt.subplots()
    ax.plot(data_arr)
    plt.title(title)

    
    

## TITLE
add_space()
print("The Array")
add_space()


The_Array = [9,8,7,6,5,4,3,2,1,0]
print("The Array: ", The_Array , "Array Address: ",id(The_Array))
print("Indexable means the array can be ref at any index.\n")

# 3 random instances of getting the array vlaue at an index

for x in range(NUM_ARRAY_DRAWS):
    print_arr_rand_index(The_Array, RAND_PICKS)


add_space()

# In python, a list could be an array and they are dynamic
# Time Complexity chart

##      Static Array    Dynamic Array(change size)
## Access   O(1)                O(1)
## Search   O(n)                O(n)
## Insert   N/A                 O(n)
## Append   N/A                 O(1)
## Delete   N/A                 O(n)
## Pop      N/A                 O(1)

## Can be used as Queues: FIFO
## Can be used as Stacks: LIFO

# Set up some charts

## Assign numbers randomly 0 -9; 10,000 times BIG_ARRAY
for i in range(BIG_ARRAY_SIZE-1):
    BIG_ARRAY.append(random.randint(0,9))
# print(BIG_ARRAY)

# Testing with the BIG array
# How long does it take to search for an item in the Big Array? 100 times
for x in range(10000):
    time_arr_access(BIG_ARRAY, BIG_ARRAY_SEARCH_TIMES)

for x in range(10000):
    time_arr_insert_replace(BIG_ARRAY, BIG_ARRAY_INSERT_TIMES)

# How long does it take to insert an item in the BIG Array?

# print collected data
    # print(BIG_ARRAY_SEARCH_TIMES)
# plot collected data
plot_data(BIG_ARRAY_SEARCH_TIMES, "Search 10,000")
plot_data(BIG_ARRAY_INSERT_TIMES, "Insert 10,000")

# Clean up the BIG array
BIG_ARRAY = []

## Assign randomly 0 -9; 100,000 times BIGGER_ARRAY
for i in range(BIGGER_ARRAY_SIZE-1):
    BIGGER_ARRAY.append(random.randint(0,9))
#print(BIGGER_ARRAY)

# Testing with the Bigger array
for x in range(10000):
    time_arr_access(BIGGER_ARRAY, BIGGER_ARRAY_SEARCH_TIMES)

for x in range(10000):
    time_arr_insert_replace(BIGGER_ARRAY, BIGGER_ARRAY_INSERT_TIMES)


## Plot the data

plot_data(BIGGER_ARRAY_SEARCH_TIMES, "Search 100,000")
plot_data(BIGGER_ARRAY_INSERT_TIMES, "Insert 100,000")


# clean up the Bigger array


# Show the charts
plt.show()


## Quick notes about array use
#### Sequential data
#### Often temp object storage
#### IO Routines
#### Lookup tables, inverse lookup tables
#### Return mult vals from function
#### cache answers to sub-problems
#### in python use tuple for lists that don't need or should not be modified





