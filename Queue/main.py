from queue import Queue


def main():
    q = Queue()
    q.push(1)
    q.push(2)
    q.push(3)
    q.push(4)
    q.push(5)

    q.print()

    q.pop()
    q.pop()
    q.print()


if __name__ == "__main__":
    main()