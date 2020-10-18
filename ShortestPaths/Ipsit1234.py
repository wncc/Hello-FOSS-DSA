# Floyd Warshall Algorithm is being used to find the shortest path in this file.
class MyGraph:

    def __init__(self, n):
        self.n = n  # number of nodes
        self.d = [[1e7 for i in range(1, n + 1)] for j in
                  range(1, n + 1)]  # The matrix to store all pairs shortest distances
        for i in range(n):
            self.d[i][i] = 0

    def insert_edge(self, i, j, w=1):
        self.d[i - 1][j - 1] = w

    def shortest_path(self, s, t):
        # Floyd Warshall Algorithm
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    self.d[i][j] = min(self.d[i][j], self.d[i][k] + self.d[k][j])

        if self.d[s - 1][t - 1] == 1e7:
            return -1
        else:
            return self.d[s - 1][t - 1]


def main():
    f = open('test.in', 'r')
    lines = f.readlines()
    lines = [i.rstrip('\n') for i in lines]
    testcase_start = []
    for i in range(len(lines)):
        if len(lines[i].split()) == 2 and len(lines[i + 1].split()) == 2:
            testcase_start.append(i)
    for i in testcase_start:
        n = int(lines[i].split()[0])
        graph = MyGraph(n)
        m = int(lines[i].split()[1])
        s = int(lines[i + 1].split()[0])
        t = int(lines[i + 1].split()[1])
        for p in range(m):
            uvw = lines[p + i + 2].split()
            u = int(uvw[0])
            v = int(uvw[1])
            w = int(uvw[2])
            graph.insert_edge(u, v, w)
        print(graph.shortest_path(s, t))
    f.close()


if __name__ == '__main__':
    main()
