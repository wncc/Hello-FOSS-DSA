## Segment Tree

The aim of this directory is to create an implementation of a segment tree to handle range sum queries.  You will initially create a segment tree for `n` elements of size `n` each initialised to 0. The queries will involve updating the value of a particular element in the segment tree and then summing over a range. Each operation needs to be logarithmic in `n`.

Your submission must be of the form `github-username.py`. You can create this file in the current directory. Your submission must either inherit the interface given in the Python file or implement a class having atleast the methods given in the interface. This Class must have the same name and methods as given in the interface.

You have to ensure that your implemenation gives the correct output on `test.in`, that is it matches with `test.out`. The input format and problem description is given as follows:

### Problem Statement

Your segment tree implementation will handle `n` elements. The queries will involve updating the value of a particular element in the segment tree or summing over a range. This needs to be fast and a naive approach will not work! Google segment tree for range queries to get more inforamtion

### Input Format

The first line contains `t`, the number of test cases.
The first line of each testcase contains `n`, the size of the segment tree and  `q`, the number of queries.

Each line of the query will begin with a query code: `U` or `S` followed by two numbers.
The queries can be of three types:
1. Update `U`: There will be a number `i` and a value `V` following this. You have to set `SegTree[i]` to `V`
2. Query `Q`: There will be two numbers `L` and `R` following this. You have to print the sum from `L` to `R` of the elements in the segment tree. Endpoints are included.
