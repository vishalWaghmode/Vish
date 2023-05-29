matrix = [
    [0, 1, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 0, 1],
    [0, 0, 0, 1, 0]
]
def DFS(matrix:list,node:int,visited:set):
    if node in visited:
        return
    visited.add(node)
    print(node)
    for n in range(len(matrix[node])):
        if matrix[node][n] == 1 and n not in visited:
            DFS(matrix,n,visited)
print("DFS Output : ")
DFS(matrix,0,set())

def BFS(matrix,node):
    quee = [node]
    visited = set([node])
    while quee:
        element = quee.pop(0)
        print(element)
        for n in range(len(matrix)):
            if matrix[element][n] == 1 and n not in visited:
                visited.add(n)
                quee.append(n)
print("BFS Output : ")
BFS(matrix,0)
            


