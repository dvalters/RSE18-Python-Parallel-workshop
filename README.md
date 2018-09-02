# The Hitchhiker's Guide to Parallelism with Python

_Workshop run at EuroSciPy 2018, Trento, Italy and Research Software Engineers conference 2018, Birmingham, England._


## Workshop contents

The workshop can be followed along using an IPython console, or Jupyter notebook, or whichever your preferred method of running Python is. For experimenting with these tutorials, I recommend a Jupyter notebook as it willallow you to use profiling tools like `timeit` and easier compilation of Cython code. However, it is up to you. 

These links below will take you to a nicely rendered, non-interactive, version of the tutorial. If you wish to run/edit the Jupyter notebooks themselves, navigate to the `workshop_notebooks` folder.

Apart from the introduction, it is not not necessary to follow the Parts in the order given - you can 'pick and mix'.

0. [Introduction to Workshop](https://nbviewer.jupyter.org/github/dvalters/RSE18-Python-Parallel-workshop/blob/master/workshop_notebooks/Introduction.ipynb)
1. [Part 1: Multiprocessing](https://nbviewer.jupyter.org/github/dvalters/RSE18-Python-Parallel-workshop/blob/master/workshop_notebooks/Part1_Multiprocessing.ipynb)
2. [Part 2: Numba](https://nbviewer.jupyter.org/github/dvalters/RSE18-Python-Parallel-workshop/blob/master/workshop_notebooks/Part2_Numba.ipynb)
3. [Part 3: Cython and parallelism](https://nbviewer.jupyter.org/github/dvalters/RSE18-Python-Parallel-workshop/blob/master/workshop_notebooks/Part4_CythonOpenMP.ipynb)
4. [Part 4: mpi4py](https://nbviewer.jupyter.org/github/dvalters/RSE18-Python-Parallel-workshop/blob/master/workshop_notebooks/Part3_MPI4py.ipynb)
5. [Discussion and Conclusions](https://nbviewer.jupyter.org/github/dvalters/RSE18-Python-Parallel-workshop/blob/master/workshop_notebooks/Conclusions.ipynb)


### Notes for setting up the VM from the RSE workshop

_This only applies if you are using the RSE 2018 Virtual Machine image_

The RSE conference organisers have provided a Virtual Machine with all the necessary Python packages pre-installed. When importing the VM disk image and setting up VirtualBox, set the number of cores to 4 (or greater) for better performance of the parllel code. (The default is 2 - it's fine to use the default, but you may not see particularly good parallel speed up from the code examples.)

When the VM is booted, navigate to `~/valters` and run:

```
git pull origin master 
```
To get the latest version of the tutorial. Then:

```
source conda.sh
conda activate intel_env
```

Now the required Python packages will be available.

## Installation and testing of python packages notes


The `install_log.txt` contains all the steps used to set up the VM (apt installs, conda install etc)

The `package-list.txt` lists all the conda packages installed in the environment.

The tests to check the packages are working correctly are in the `test_workshop_VM` folder

 - Run the script `run_all_workshop_tests.sh` from that directory.
 - They can also be run individually from within each subdirectory if needed.
 - The full correct outputs are in `test_correct_ouput_log.txt`
 - There should be no Python tracebacks or import errors if everything runs correctly.



