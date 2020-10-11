class SegmentTree:
	def __init__(self, n):
		#create segment tree of n elements [1, n]
		raise NotImplementedError

	def update(self, i, count=1):
		#update element at index i with value count
		raise NotImplementedError

	def query(self, l, r):
		#find sum in range[l, r] in the segment tree
		raise NotImplementedError

	def reset(self, number):
		#reset segment tree
		raise NotImplementedError


def main():
	f = open("test.in", "r")
	## handle input here from f 
	st = SegmentTree()

	# handle operations and print to terminal

	f.close()

if __name__=='__main__':
	main()