#!/usr/bin/env bash

cd test_cython_basic
./run_tests.sh
cd ..

cd test_cython_openmp
./run_tests.sh
cd ..

cd test_mpi4py
./run_tests.sh
cd ..

cd test_multiprocessing
./run_tests.sh
cd ..

cd test_numba
./run_tests.sh
cd ..

