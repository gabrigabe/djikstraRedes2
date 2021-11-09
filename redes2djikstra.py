from queue import PriorityQueue

A = 1
B = 2
C = 3
D = 4
E = 5
F = 6
G = 7

class Graph:


    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)]
                      for j in range(num_of_vertices)]
        self.visited = []

    def add_edge(self, u, v, path):
        self.edges[u][v] = path

    def dijkstra(self, start_vertex):
        Dj = {v: float('inf') for v in range(self.v)}
        Dj[start_vertex] = 0

        pq = PriorityQueue()
        pq.put((0, start_vertex))

        while not pq.empty():
            (dist, current_vertex) = pq.get()
            self.visited.append(current_vertex)

            for neighbor in range(self.v):
                if self.edges[current_vertex][neighbor] != -1:
                    distance = self.edges[current_vertex][neighbor]
                    if neighbor not in self.visited:
                        old_cost = Dj[neighbor]
                        new_cost = Dj[current_vertex] + distance
                        if new_cost < old_cost:
                            pq.put((new_cost, neighbor))
                            Dj[neighbor] = new_cost
        return Dj


gr = Graph(8)
gr.add_edge(A, B, 7)
gr.add_edge(A, D, 5)
gr.add_edge(B, C, 8)
gr.add_edge(B, D, 9)
gr.add_edge(B, E, 7)
gr.add_edge(C, E, 5)
gr.add_edge(D, E, 15)
gr.add_edge(D, F, 6)
gr.add_edge(F, D, 8)
gr.add_edge(F, G, 11)
gr.add_edge(G, E, 9)

Dj = gr.dijkstra(1)

for vertex in range(len(Dj)):
    router = '';
    if vertex == 1:
      router = 'A'
    elif vertex == 2:
      router = 'B'
    elif vertex == 3:
      router = 'C'
    elif vertex == 4:
      router = 'D'
    elif vertex == 5:
      router = 'E'
    elif vertex == 6:
      router = 'F'
    elif vertex ==7:
      router = 'G'
    if vertex >=1:
     print("A menor rota do roteador A para o roteador", router, "é", Dj[vertex])
 