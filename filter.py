from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = [1,2,3,4,5]
else:
    data = []

#function
def function(n):
	return n%2 == 0

#Scatter
data = comm.scatter(data, root=0)
print("rank", rank, "recieved", data)
if not function(data):
	data = None

#Gather
data = comm.gather(data, root=0)

comm.Barrier()

if rank == 0:
    print(data)