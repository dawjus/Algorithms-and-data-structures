# Dawid Justyna
# Algorytm polega na tym, że dla każdego zamku sprawdzam najtańszy koszt (algorytmmem Dijkstry) ile kosztuje dojazd do tego zamku
# potem odejmuje zysk jaki tam moge zrobić i nastepnie
# Wykonuje dwa razy Dijkstre raz od początku grafu, a następnie od końca na nowym grafie. Następnei sprawdzam w którym momencie opłaca
# się obrabować zamek
# Nowy graf tworze funkcja create_graph i przechodze po starym grafie i popsorptu zwiekszam wartosc krawedzi 2krotnie i dodaje r.
# Złożonosć obliczeniowa dijkstra Elog(V)  a całość Elog(V) + E

from queue import PriorityQueue

def gold(G,V,s,t,r):
  n = len(G)
  G2 = create_graph(G,r)
  cost_before_theft = dijkstra(G,s)
  cost_after_theft = dijkstra(G2,t)
  cost = [0 for _ in range(n)]
  for i in range(n):
    cost[i] = cost_before_theft[i] + cost_after_theft[i] - V[i]
  return min(cost)

def create_graph(G,r):
  n = len(G)
  G2 = [[] for i in range(n)]
  for i in range(n):
    for j in range(len(G[i])):
      G2[i].append((G[i][j][0], G[i][j][1]*2+r))
  return G2

def relax(distance, parent, u, v):
    if distance[v[0]] > distance[u] + v[1]:
        distance[v[0]] = distance[u] + v[1]
        parent[v[0]] = u
        return True
    return False

def dijkstra(G, s):
    n = len(G)
    Q = PriorityQueue()
    parent = [None for _ in range(n)]
    distance = [float("inf") for _ in range(n)]
    visited = [False for _ in range(n)]
    Q.put((0, s))
    distance[s] = 0
    while not Q.empty():
        dist, u = Q.get()
        visited[u] = True
        for v in G[u]:
            if not visited[v[0]] and relax(distance, parent, u, v):
                Q.put((dist + v[1], v[0]))
    return distance

