import sys
sys.setrecursionlimit(5000)  
class Graph:
    
    def __init__(self, n):
        # create Graph of n nodes [1, n]
        self.n = n
        self.graph = []
        self.visited = []
        for i in range(n):
            self.graph.append([])
            self.visited.append(0)
        return  
        # raise NotImplementedError

    def insert_edge(self, i, j):
        # insert edge between i to j (undirected)
        self.graph[i].append(j)
        self.graph[j].append(i)
        return
        raise NotImplementedError
        
    def dfs(self, i):
        if(self.visited[i]==0):
            self.visited[i] = 1
            for j in range(len(self.graph[i])):
                node = self.graph[i][j]
                
                if(self.visited[node]==0):
                    self.dfs(node)
        return
    def connected_components(self):
        # return number of connected components
        res = 0
        for i in range(self.n):
            if (self.visited[i]==0):
                self.dfs(i)
                res+=1
        return res
        #raise NotImplementedError


def main():
    f = open("test.in", "r")
    # handle input here from f
    t = int(f.readline())
    for i in range(t):
        nm = f.readline()
        n = int(nm.split(" ")[0])
        m = int(nm.split(" ")[1])
        graph = Graph(n)
        for p in range(m):
            ij = f.readline()
            i = int(ij.split(" ")[0])
            j = int(ij.split(" ")[1])
            graph.insert_edge(i-1,j-1)
        
        print(graph.connected_components())
        del graph
        # print(graph.graph[0],graph.visited[0])
    # handle operations and print to terminal

    f.close()

if __name__ == '__main__':
    main()
