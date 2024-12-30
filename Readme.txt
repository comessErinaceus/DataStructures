Python implementation of data structures

Use a python virtual env
    python3 -m venv venv

check your python packages
    pip freeze
    pip list

python packages used
    1. plotext


Different lang will have different considerations
    i.e python lists are dynamic, C++ can create static or dynamic arrays
        int arr[6]; -- Static C++ array with 6 ints
        int* arr = new int[5]; -- Dynamic array with 5 integers

        Consider memory allocation costs/tradeoffs in type of data struct, and where that container is located Stack vs Heap
        -- With python... this is less of a consideration