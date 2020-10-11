## Balanced Binary Search Tree

The aim of this directory is to create an implementation of a self balancing binary search tree in Python. This has to be self balancing, you can use AVL or Red Black Tree or Treaps as long as it is efficient.

Your submission must be of the form `github-username.py`. You can create this file in the current directory. Your submission must either inherit the interface given in the Python file or implement a class having atleast the methods given in the interface. This Class must have the same name and methods as given in the interface.

You have to ensure that your implemenation gives the correct output on `test.in`, we will be checking this. The input format and problem description is given as follows:

### Problem Statement

Your BST implementation must be able to remove and insert numbers into the BST and find the smallest number in the BST greater than a query number which will be asked in the input. For instance if your BST contains `2 4 5 6 8` then querying `7` should output and print `8` to the terminal while querying `5` should output `5`. If the query is `9` the output will be `-1`. The numbers are guaranteed to be non negative.

### Input Format

The first line contains `t`, the number of test cases.
The first line of each testcase contains `q`, the number of queries.

Each line of the query will begin with a query code: `I`, `R` or `G`, followed by a number.
The queries can be of three types:
1. Insert `I`: The number following this code will be the number to insert into the BST 
2. Remove `R`: The number following this code will be the number to remove from the BST
2. Greater than or Equal To `G`: The number following this code will be the query number for the BST. At the end of this query, you have to print the result of the query to the terminal.

It maybe possible that the number to remove is not there in the BIT anymore, in this case do nothing!