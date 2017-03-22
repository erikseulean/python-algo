from Traversal.traversal import Traversal

def main():

    Matrix = [0 for i in range(7)]
    Matrix[0] = [0, 1, 0, 0, 0 ,0, 0]
    Matrix[1] = [1, 0, 0, 1, 1, 0, 0]
    Matrix[2] = [0, 0, 0, 1, 0, 1, 1]
    Matrix[3] = [0, 1, 1, 0, 0, 0, 0]
    Matrix[4] = [0, 1, 0, 0, 0, 1, 0]
    Matrix[5] = [0, 0, 1, 0, 1, 0, 1]
    Matrix[6] = [0, 0, 1, 0, 0, 1, 0]

    it = Traversal()
    it.bfs(0, Matrix)
    print("")
    it.dfs(0, Matrix)


if __name__ == "__main__":
    main()
