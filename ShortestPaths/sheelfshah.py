import sys


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.weights = [[0 for column in range(vertices)]
                        for row in range(vertices)]

    def closest_next_point(self, distance, visited):
        min_ = sys.maxsize
        for v in range(self.V):
            if distance[v] < min_ and visited[v] == False:
                min_ = distance[v]
                min_index = v

        try:
            return min_index
        except:
            return -1

    def dijkstra(self, s):

        distance = [sys.maxsize] * self.V
        distance[s] = 0
        visited = [False] * self.V

        for _ in range(self.V):
            u = self.closest_next_point(distance, visited)
            if u == -1:
                return [-1] * self.V
            visited[u] = True
            for v in range(self.V):
                if self.weights[u][v] > 0 and visited[v] == False and distance[v] > distance[u] + self.weights[u][v]:
                    distance[v] = distance[u] + self.weights[u][v]
        return distance

    def insert_edge(self, i, j, w=1):
        self.weights[i][j] = w
        self.weights[j][i] = w

    def shortest_path(self, s, t):
        if s == t:
            return 0
        distances = self.dijkstra(s)
        return distances[t]


def my_split(string):
    return string.split()


def main():
    f = open("test.in", "r")
    t = int(f.readline())
    for _ in range(t):
        n, m = list(map(int, f.readline().split()))
        start, end = list(map(int, f.readline().split()))
        g = Graph(n)
        for _ in range(m):
            u, v, w = list(map(int, f.readline().split()))
            g.insert_edge(u - 1, v - 1, w)
        ans = g.shortest_path(start - 1, end - 1)
        print(ans)
    f.close()

if __name__ == '__main__':
    main()
