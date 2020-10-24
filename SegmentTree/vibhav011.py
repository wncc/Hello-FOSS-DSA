class SegmentTree:
	def __init__(self, n):
		self.N = n					# Length of array
		self.st = [0] * 2*n			# Initialized to 0

	def update(self, i, count=1):
		i += self.N
		self.st[i] = count
		while i > 1:
			self.st[i//2] = self.st[i] + self.st[i^1]
			i = i//2

	def query(self, l, r):
		ans = 0;
		l += self.N
		r += self.N
		while l < r:
			if l&1:
				ans += self.st[l];
				l += 1
			if r&1:
				r -= 1
				ans += self.st[r];
			l = l//2
			r = r//2
		return ans

	def reset(self, number):
		self.N = 0
		self.st = []


def main():
	f = open("test.in", "r")

	t = int(f.readline())

	for i in range(t):
		n, q = list(map(int, f.readline().split()))
		st = SegmentTree(n)
		for j in range(q):
			Q, a, b = f.readline().split()
			if Q == 'U':
				st.update(int(a)-1, int(b))
			else:
				print(st.query(int(a)-1, int(b)))

		del st

	f.close()

if __name__=='__main__':
	main()