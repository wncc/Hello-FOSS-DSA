class SegmentTree:
	def __init__(self, n=1):
		#create segment tree of n elements [1, n]
		tree = []
		for i in range(4*n+4):
			tree.append(0)
		self.tree = tree
		self.n = n
		# raise NotImplementedError

	def update(self, i, count=1):
		#update element at index i with value count
		self.tree_update(1,1,self.n,i,count)
		# raise NotImplementedError

	def tree_update(self,node,l,r,i,count):
		if (l == r):
			self.tree[node] = count
		else:
			mid = int((l+r)/2)
			if (i <= mid):
				self.tree_update(2*node,l,mid,i,count)
			else:
				self.tree_update(2*node+1,mid+1,r,i,count)
			self.tree[node] = self.tree[2*node]+self.tree[2*node+1]

	def query(self, l, r):
		#find sum in range[l, r] in the segment tree
		return self.tree_query(1,1,self.n,l,r)
		# raise NotImplementedError
		
	def tree_query(self,node,l,r,st,en):
		if ((l > en) or (r < st)):
			return 0
		elif (l >= st and r <= en):
			return self.tree[node]
		else:
			mid = int((l+r)/2)
			ans1 = self.tree_query(2*node,l,mid,st,en)
			ans2 = self.tree_query(2*node+1,mid+1,r,st,en)
			return ans1+ans2

	def reset(self, number):
		#reset segment tree
		# raise NotImplementedError
		tree = []
		for i in range(4*number+4):
			tree.append(0)
		self.tree = tree
		self.n = number


def main():
	f = open("test.in", "r")
	## handle input here from f 
	st = SegmentTree()
	test_cases = int(f.readline())
	for i in range(test_cases):
		n, q = f.readline().split()
		n, q = int(n), int (q)
		st.reset(n)
		for j in range(q):
			s = f.readline().split()
			if (s[0] == 'U'):
				st.update(int(s[1]), int(s[2]))
			else:
				print(st.query(int(s[1]), int(s[2])))
	# handle operations and print to terminal

	f.close()

if __name__=='__main__':
	main()