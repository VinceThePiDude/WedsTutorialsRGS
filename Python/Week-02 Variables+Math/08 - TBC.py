def Main():
    x = 20
    print("X is", x)
    def add():
        global x
        x = 10
        print("X is", x, "In add")

    add()
Main()
print("X is", x, "after add")
