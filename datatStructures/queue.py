# Simple Queue
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def peek(self):
        return self.items(len(self.items) - 1)

    def enqueue(self, item):
        #  Inserts each new element at the head
        self.items.insert(0, item)

    def dequeue(self):
        if(len(self.items) > 0):
            self.items.pop()
        else:
            print("No item to dequeue")

    def show(self):
        print(self.items[:])


def run():
    q = Queue()
    q.enqueue(10)
    q.show()
    q.enqueue(1.324)
    q.show()
    q.enqueue("Hello, world!!!")
    q.show()
    q.enqueue(["Comp Sci", 4])
    q.show()
    q.dequeue()
    print("Dequeued")
    q.show()
    q.show()


run()

