# python3

# Dijkstra’s algorithm using adjacency list and priority queue using binary heap
# Total Running Time: T(MakeQueue) + |V| · T(ExtractMin) + |E| · T(ChangePriority)
# O(|V| + (|V| · log|V|) + (|E| · log|V|)) = O((|V| + |E|) log|V|) 

import math

class Edge:
	def __init__(self, to:int, cost:int):
		"""
			to: where the edge is going
			cost: weight of the path
		"""
		self.to = to
		self.cost = cost


class Graph:
	def __init__(self, n):
		# create Graph of n nodes [1, n]
		"""
			n : number of nodes in the graph
			adj: adjacency list
		"""
		self.n = n
		self.adj = [[] for _ in range(n)]
		
	def insert_edge(self, i, j, w=1):
		# insert edge between i to j of weight w 
		self.adj[i].append(Edge(j, w))

	def shortest_path(self, s, t):
		distance = [math.inf for _ in range(self.n)]
		distance[s] = 0
		# prev = [None for _ in range(self.n)]
		# prev[s] = s
		h = PriorityQueue()
		for i in range(self.n):
			h.insert(Node(i, distance[i]))
		while len(h.GetQ()) > 0:
			u = h.extract_min()
			vertex = u.vertex
			for neighbour in self.adj[vertex]:
				if distance[neighbour.to] > distance[vertex] + neighbour.cost:
					distance[neighbour.to] = distance[vertex] + neighbour.cost
					# prev[neighbour.to] = vertex
					h.ChangePriority(h.map[neighbour.to], distance[neighbour.to])
		return -1 if distance[t] == math.inf else distance[t]


class Node:
	def __init__(self, i: int, val:int):
		self.vertex = i
		self.value = val


class PriorityQueue:
	def __init__(self):
		self.pq = []
		self.map = {}

	def GetQ(self):
		return self.pq

	@staticmethod
	def GetLeftChild(i: int) -> int:
		return 2 * i + 1

	@staticmethod
	def GetRightChild(i: int) -> int:
		return 2 * i + 2

	@staticmethod
	def GetParent(i: int) -> int:
		return (i - 1) // 2	

	def sift_up(self, i:int):
		q = self.GetQ()
		parent = PriorityQueue.GetParent(i)
		while i > 0 and q[parent].value > q[i].value:
			q[parent], q[i] = q[i], q[parent]
			self.map[q[i].vertex] = i
			self.map[q[parent].vertex] = parent
			i = parent
			parent = PriorityQueue.GetParent(i)
	
	def sift_down(self, i:int):
		q = self.GetQ()
		min_index = i
		left = PriorityQueue.GetLeftChild(i)
		right = PriorityQueue.GetRightChild(i)
		if left < len(q) and q[left].value < q[min_index].value:
			min_index = left
		if right < len(q) and q[right].value < q[min_index].value:
			min_index = right
		if min_index != i:
			q[min_index], q[i] = q[i], q[min_index]
			self.map[q[min_index].vertex] = min_index
			self.map[q[i].vertex] = i
			self.sift_down(min_index)
	
	def extract_min(self):
		q = self.GetQ()
		q[len(q) - 1], q[0] = q[0], q[len(q) - 1]
		self.map[q[len(q) - 1].vertex] = len(q) - 1
		self.map[q[0].vertex] = 0
		value = q.pop()
		del self.map[value.vertex]
		self.sift_down(0)
		return value
	
	def ChangePriority(self, i: int, new_priority):
		q = self.GetQ()
		old_priority = q[i].value
		q[i].value = new_priority
		if new_priority < old_priority:
			self.sift_up(i)
		elif new_priority > old_priority:
			self.sift_down(i)

	def insert(self, element:list):
		self.pq.append(element)
		self.map[element.vertex] = len(self.pq) - 1
		self.sift_up(len(self.pq) - 1)
	

def main():
	f = open("test.in", "r")
	t = int(f.readline())
	for _ in range(t):
		n, m = map(int, f.readline().split())
		s, t = map(int, f.readline().split())
		s, t = s - 1, t - 1
		g = Graph(n)
		for _ in range(m):
			u, v, w = map(int, f.readline().split())
			g.insert_edge(u - 1, v - 1, w)
			g.insert_edge(v - 1, u - 1, w)
		print(g.shortest_path(s, t))
	f.close()

if __name__=='__main__':
	main()
