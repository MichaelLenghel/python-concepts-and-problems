# Simple Stack
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        if len(self.items) > 0:
            self.items.pop(0)
        else:
            print("No item to pop")

    def peek(self):
        self.items.remove(len(self.items) - 1)

    def size(self):
        return len(self.items)

    def show(self):
        print(self.items[:])

def run():
    s = Stack()
    try:
        s.pop()
    except:
        print("Could not remove element")
    s.push(15)
    s.show()
    s.push("Dog")
    s.show()
    s.push(1.534)
    s.show()
    s.push(1)
    s.show()
    s.pop()
    s.show()

run()





