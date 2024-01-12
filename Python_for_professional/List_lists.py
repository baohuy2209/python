class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, val):
        self.data = val

    def setNext(self, next):
        self.next = next


class ListedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def add(self, item):
        new_node = Node(item)
        if self.isEmpty():
            new_node.setNext(None)
            self.head = new_node
        else:
            new_node.setNext(self.head)
            self.head = new_node

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        if current is None:
            return found
        while current is not None and found is not True:
            if current.getData() is item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while current is not None and found is not True:
            if current.getData() is item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if found:
            if previous is None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())
        else:
            raise ValueError("Value not found ... ")

    def insert(self, position, item):
        if position < 0 or position > self.size() - 1:
            raise IndexError("Index out of bounds")
        else:
            current = self.head
            previous = None
            pos = 0
            while pos < position:
                pos += 1
                previous = current
                current = current.getNext()
            new_node = Node(item)
            previous.setNext(new_node)
            new_node.setNext(current)

    def index(self, item):
        if self.search(item) is False:
            return -1
        else:
            current = self.head
            pos = 0
            found = False
            while current is not None and found is False:
                if current.getData() is item:
                    found = True
                else:
                    current = current.getNext()
                    pos += 1
        return pos

    def pop(self, position=None):
        if position < 0 and position > self.size() - 1:
            raise IndexError("Index out of bounds")
        else:
            current = self.head
            if position is None:
                ret = current.getData()
                self.head = current.getNext()
            else:
                pos = 0
                previous = None
                while pos < position:
                    previous = current
                    current = current.getNext()
                    pos += 1
                    ret = current.getData()
                previous.setNext(current.getNext)
                print(ret)
        return ret

    def append(self, item):
        new_node = Node(item)
        if self.isEmpty():
            self.head = new_node
        else:
            previous = None
            current = self.head
            while current is not None:
                previous = current
                current = current.getNext()
            previous.setNext(new_node)

    def printList(self):
        current = self.head
        print("Current single linked list : ")
        while current is not None:
            print(current.getData() + " ")
            current = current.getNext()


if __name__ == "__main__":
    ll = ListedList()
