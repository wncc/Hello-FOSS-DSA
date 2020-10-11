## Connected Components

The aim of this directory is to create an implementation of a graph that is able to output the number of connected components in the graph. The implementation needs to be EFFICIENT!

Your submission must be of the form `github-username.py`. You can create this file in the current directory. Your submission must either inherit the interface given in the Python file or implement a class having atleast the methods given in the interface. This Class must have the same name and methods as given in the interface.

You have to ensure that your implemenation gives the correct output on `test.in`, that is it matches with `test.out`. The input format and problem description is given as follows:

### Problem Statement

Your Graph implementation will have `n` nodes and `m` edges. At the end of a test case you have to print a single integer, the number of connected components in the graph in this test case.

### Input Format

The first line contains `t`, the number of test cases.
The first line of each testcase contains `n`, the number of nodes (from `1` to `n`) and `m` the number of edges.

`m` lines will follow with two integers `u` and `v` denoting that there is an edge between `u` and `v`.

At the end of each test case output the number of connected components in the graph.
