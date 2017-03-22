from list_stack import ListStack


def main():
    s = ListStack(100)
    s.push(5)
    s.push(3)
    s.push(7)
    s.push(10)
    s.print()
    s.pop()
    s.print()
    s.pop()
    s.print()

if __name__ == "__main__":
    main()
