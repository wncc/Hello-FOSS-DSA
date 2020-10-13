import sys
sys.setrecursionlimit(10**5)


class Graph:

    def __init__(self, n):
        self.connections = {}
        self.num_vertices = n
        self.visited = [False] * n
        for i in range(0, n):
            self.connections[i] = []

    def insert_edge(self, i, j):
        self.connections[i].append(j)
        self.connections[j].append(i)

    def visit_dfs(self, v, already_connected):
        self.visited[v] = True
        already_connected.append(v)

        for neighbor in self.connections[v]:
            if not self.visited[neighbor]:
                # append visited nodes to already_connected
                already_connected = self.visit_dfs(neighbor, already_connected)
        return already_connected

    def connected_components(self):
        ans = 0
        for v in range(self.num_vertices):
            if not self.visited[v]:
                self.visit_dfs(v, [])
                ans += 1
        return ans


def my_split(string):
    return string.split()


def main():
    f = open("test.in", "r")
    t = int(f.readline())
    for _ in range(t):
        n, m = list(map(int, f.readline().split()))
        g = Graph(n)
        for _ in range(m):
            u, v = list(map(int, f.readline().split()))
            g.insert_edge(u - 1, v - 1)
        ans = g.connected_components()
        print(ans)
    f.close()

if __name__ == '__main__':
    main()
