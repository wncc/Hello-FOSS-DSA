class BIT:
	def __init__(self, n):
		#create BIT of n elements [1, n]
		raise NotImplementedError

	def update(self, i, count=1):
		#update element at index i with value count
		raise NotImplementedError

	def query(self, l, r):
		#find sum in range[l, r] in the BIT
		raise NotImplementedError

	def reset(self, number):
		#reset BIT
		raise NotImplementedError


def main():
	f = open("test.in", "r")
	## handle input here from f 
	bit = BIT()

	# handle operations and print to terminal

	f.close()

if __name__=='__main__':
	main()