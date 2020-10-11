class Graph:
	def __init__(self, n):
		#create Graph of n nodes [1, n]
		raise NotImplementedError

	def insert_edge(self, i, j, w=1):
		#insert edge between i to j of weight w (undirected)
		raise NotImplementedError

	def mst(self):
		#return sum of edges in Minimum Spanning tree
		raise NotImplementedError


def main():
	f = open("test.in", "r")
	## handle input here from f 
	graph = Graph()

	# handle operations and print to terminal

	f.close()

if __name__=='__main__':
	main()