class BalancedBinarySearchTree:
	def __init__(self):
		raise NotImplementedError

	def insert(self, number):
		#insert number to BST
		raise NotImplementedError

	def remove(self, number):
		#remove number from BST
		raise NotImplementedError

	def greater_than_equal(self, number):
		#find number in BST greater than equal to number. Return -1 if does not exist.
		raise NotImplementedError


def main():
	f = open("test.in", "r")
	## handle input here from f 
	bst = BalancedBinarySearchTree()

	# handle operations and print to terminal

	f.close()

if __name__=='__main__':
	main()