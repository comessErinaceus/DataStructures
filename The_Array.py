## Fixed length container of n elements usually indexable from the range [0, n-1], sometimes contiguous memory depending on language

## Imports
import random
# import plotext as plt
# import numpy as np


## GLOBAL VARS
#spacer = ("#----------###----------#\n")
NUM_ARRAY_DRAWS = random.randint(1 , 6)
RAND_PICKS = []


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


## TO-DO Use plotly to plot the time complexity of arrays -- pattern will only emerge with large enough data sets
# Sample sin wave
# x = np.linspace(0, 10, 100)
# y = np.sin(x)

# plt.plot(x,y)

# plt.show()


## Quick notes about array use
#### Sequential data
#### Often temp object storage
#### IO Routines
#### Lookup tables, inverse lookup tables
#### Return mult vals from function
#### cache answers to sub-problems
#### in python use tuple for lists that don't need or should not be modified





