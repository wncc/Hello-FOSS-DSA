class Graph:
	def __init__(self, n):
		#create Graph of n nodes [1, n]
		raise NotImplementedError

	def insert_edge(self, i, j):
		#insert edge between i to j (undirected)
		raise NotImplementedError

	def connected_components(self):
		#return number of connected components
		raise NotImplementedError


def main():
	f = open("test.in", "r")
	## handle input here from f 
	graph = Graph()

	# handle operations and print to terminal

	f.close()

if __name__=='__main__':
	main()