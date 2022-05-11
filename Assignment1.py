

path=[]
vertices=set()
edges=set()
graph = dict()
def take_input():
  n=int(input("Enter number of vertices : "))

  for v in range(n):
    v=input("Enter Vertex : ")
    vertices.add(v)
    print("Vertex",v,"added.")
  
  n1=int(input("Enter number of edges : "))

  for e in range(n1):
    print("Enter starting vertex of edge",e+1," : ")
    v1=input()
    print("Enter ending vertex of edge",e+1," : ")
    v2=input()
    edge=(v1,v2)
    edges.add(edge)
    print("Edge",edge,"added.")


    
    
def create_graph(vertices,edges):
  for vertex in vertices:
    graph[vertex]=[]

  for edge in edges:
    v1=edge[0]
    v2=edge[1]
    graph[v1].append(v2)
    graph[v2].append(v1)

  print("The Graph : ",graph)


visited_dfs=set() 

def DFS(visited, graph, node):  
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            DFS(visited, graph, neighbour)



visited_bfs=[]
queue=[]

def BFS(visited, graph, node): 
  visited.append(node)
  queue.append(node)

  while queue:         
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)



take_input()
create_graph(vertices,edges)

start_dfs=input("Enter starting vertex for DFS : ")
print("Result of Depth First Search")
DFS(visited_dfs,graph,start_dfs)

start_bfs=input("Enter starting vertex for BFS : ")
print("Result of Breadth First Search")
BFS(visited_bfs,graph,start_bfs)










