from queue import Queue

class Traversal(object):
    def __init__(self):
        pass

    def bfs(self, start, matrix):
        q = Queue()
        visited = [False for row in range(len(matrix))]
        q.put(start)
        visited[start] = True
        while not q.empty():
            node = q.get()
            print(node)
            for i in range(len(matrix)):
                if not visited[i] and matrix[node][i] == 1:
                    q.put(i)
                    visited[i] = True

    def dfs(self, start, matrix):
        stack = []
        visited = [False for i in range(len(matrix))]
        visited[start] = True
        stack.append(start)
        while len(stack) is not 0:
            node = stack.pop()
            print(node)
            for i in range(len(matrix)):
                if not visited[i] and matrix[node][i] == 1:
                    stack.append(i)
                    visited[i] = True
