# The Hitchhiker's Guide to Parallelism with Python

### Workshop run at EuroSciPy 2018, Trento, Italy and Research Software Engineers conference 2018, Birmingham, England.

## Workshop contents

The workshop can be followed along using an IPython console, or Jupyter notebook.

0. [Introduction to Workshop](https://nbviewer.jupyter.org/github/dvalters/RSE18-Python-Parallel-workshop/blob/master/workshop_notebooks/Introduction.ipynb)
1. [Part 1: Multiprocessing](https://nbviewer.jupyter.org/github/dvalters/RSE18-Python-Parallel-workshop/blob/master/workshop_notebooks/Part1_Multiprocessing.ipynb)
2. [Part 2: Numba](https://nbviewer.jupyter.org/github/dvalters/RSE18-Python-Parallel-workshop/blob/master/workshop_notebooks/Part2_Numba.ipynb)
3. [Part 3: mpi4py](https://nbviewer.jupyter.org/github/dvalters/RSE18-Python-Parallel-workshop/blob/master/workshop_notebooks/Part3_MPI4py.ipynb)
4. [Part 4: Cython and parallelism](https://nbviewer.jupyter.org/github/dvalters/RSE18-Python-Parallel-workshop/blob/master/workshop_notebooks/Part4_CythonOpenMP.ipynb)
5. [Conclusions](https://nbviewer.jupyter.org/github/dvalters/RSE18-Python-Parallel-workshop/blob/master/workshop_notebooks/Conclusions.ipynb)



## Installation and testing of python packages notes

The `install_log.txt` contains all the steps used to set up the VM (apt installs, conda install etc)

The `package-list.txt` lists all the conda packages installed in the environment.

The tests to check the packages are working correctly are in the `test_workshop_VM` folder

 - Run the script `run_all_workshop_tests.sh` from that directory.
 - They can also be run individually from within each subdirectory if needed.
 - The full correct outputs are in `test_correct_ouput_log.txt`
 - There should be no Python tracebacks or import errors if everything runs correctly.



