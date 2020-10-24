class BIT:
	def __init__(self, n):
		self.N = n+1					# Length of array
		self.bit = [0] * (n+1)			# Initialized to 0

	def update(self, i, count=1):
		ind = i
		count = count - self.getSum(i) + self.getSum(i-1)
		while ind <= self.N :
			self.bit[ind] += count
			ind += (ind & (-ind))

	def getSum(self, x) :
		if x <= 0 :
			return 0
		ind = x
		ans = 0
		while ind > 0:
			ans += self.bit[ind]
			ind = (ind & (ind-1))
		return ans

	def query(self, l, r):
		return self.getSum(r) - self.getSum(l-1)

	def reset(self, number):
		self.N = 0
		self.bit = []


def main():
	f = open("test.in", "r")

	t = int(f.readline())

	for i in range(t):
		n, q = list(map(int, f.readline().split()))
		bit = BIT(n)
		for j in range(q):
			Q, a, b = f.readline().split()
			if Q == 'U':
				bit.update(int(a), int(b))
			else:
				print(bit.query(int(a), int(b)))

		del bit

	f.close()

if __name__=='__main__':
	main()