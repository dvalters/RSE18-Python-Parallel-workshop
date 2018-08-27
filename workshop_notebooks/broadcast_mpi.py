import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD

print("-"*78)
print(" Running on %d cores" % comm.size)
print("-"*78)

comm.Barrier()

# Prepare a vector of N=5 elements to be broadcasted...
N = 5
if comm.rank == 0:
    A = np.arange(N, dtype=np.float64)    # rank 0 has proper data
else:
    A = np.empty(N, dtype=np.float64)     # all other just an empty array

# Broadcast A from rank 0 to everybody
comm.Bcast( [A, MPI.DOUBLE] )

# Everybody should now have the same...
print("[%02d] %s" % (comm.rank, A))
