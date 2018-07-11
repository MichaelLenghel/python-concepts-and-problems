# Simple linked list 
class Node:
    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next_node(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def insert(self, item):
        new_node = Node(item)
        new_node.set_next_node(self.head)
        self.head = new_node


    def delete(self, item):
        current = self.head
        previous = None

        while current:
            if current.get_data() == item:
                previous.set_next_node(current.get_next())
                return True
            else:
                previous = current
                current = current.get_next()

        # Node not found -> return false
        return False


    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        current = self.head
        while current:
            if item == current.get_data():
                return True
            else:
                current = current.get_next()
        return False

    def print_eles(self):
        current = self.head
        while current:
            print(current.get_data(), end=", ")
            current = current.get_next()


def run():
    _list = LinkedList()
    _list.insert(15)
    _list.insert(30)
    _list.insert(45)

    count = _list.size()
    print("Number of elements in the list: ", count)

    _list.delete(30)
    _list.print_eles()

run()