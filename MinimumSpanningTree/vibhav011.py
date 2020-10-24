class Graph:
	def __init__(self, n):
		self.v = n			# number of vertices
		self.e = []			# List of tuples of the form (u, v, w)

	def insert_edge(self, i, j, w=1):
		self.e += [(i, j, w)]

	def mst(self):
		self.e.sort(key = lambda item : item[2])		# Sort the edges list in ascending order on the basis of weight
		min_weigth = 0									# Final answer

		parent = [0]					# Parent list
		size = [0]						# if i is a root then size[i] = number of nodes in the tree else size[i] = 0
		for i in range(self.v):
			parent += [i+1]
			size += [1]

		def findRoot(u) :				# function to find root of the tree contaning u
			if parent[u] == u:
				return u
			v = findRoot(parent[u])
			parent[u] = v 				# path compression
			return v

		num_vertices = 0

		for edge in self.e :
			if num_vertices == self.v-1 : break

			root1 = findRoot(edge[0])
			root2 = findRoot(edge[1])
			if root1 != root2:
				min_weigth += edge[2]
				num_vertices += 1
				if size[root1] <= size[root2]:			# union by rank technique
					size[root2] += size[root1]
					size[root1] = 0
					parent[root1] = root2
				else:
					size[root1] += size[root2]
					size[root2] = 0
					parent[root2] = root1

		num_trees = 0					# variable to store number of trees are in the minimum spanning forest

		for i in range(self.v+1):
			if i == parent[i]:
				num_trees += 1
		if num_trees > 2:
			return -1

		return min_weigth


def main():
	f = open("test.in", "r")

	t = int(f.readline())

	for i in range(t):
		n, m = f.readline().split()
		n = int(n)
		m = int(m)
		graph = Graph(n)
		for j in range(m):
			u, v, w = f.readline().split()
			graph.insert_edge(int(u), int(v), int(w))
		print(graph.mst())
		del graph

	f.close()

if __name__=='__main__':
	main()