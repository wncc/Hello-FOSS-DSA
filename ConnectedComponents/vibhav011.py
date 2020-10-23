import sys
from collections import defaultdict

class Graph:

	def __init__(self, n):
		self.v = n		   							# number of vertices
		self.adj = defaultdict(lambda: [])			# adjacency list
		self.visited = [False] * n					# visited list

	def insert_edge(self, i, j):
		self.adj[i].append(j)
		self.adj[j].append(i)

	def dfs(self, u):
			self.visited[u] = True
			for v in self.adj[u]:
				if not self.visited[v]:
					self.dfs(v)

	def connected_components(self):
		con_comp = 0
		for i in range(self.v):
			if not self.visited[i]:
				con_comp += 1
				self.dfs(i)
		return con_comp


def main():
	sys.setrecursionlimit(10000)

	f = open("test.in", "r")

	t = int(f.readline())

	for i in range(t):
		n, m = list(map(int, f.readline().split()))
		graph = Graph(n)
		for j in range(m):
			u, v = list(map(int, f.readline().split()))
			graph.insert_edge(u-1, v-1)

		print(graph.connected_components())
		del graph

	f.close()

if __name__ == '__main__':
	main()
