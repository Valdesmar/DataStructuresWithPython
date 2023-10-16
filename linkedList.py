class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.numElems = 0

    def insert(self, data):
        newNode = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
            self.numElems += 1
        else:
            self.head = newNode
            self.numElems += 1

    def getSize(self):
        return self.numElems

    def remove(self, x):
        current = self.head
        while current:
            if current.data == x:
                current = current.next
                return
            current = current.next

    def printList(self):
        print("##############")
        current = self.head
        while(current):
            print(current.data)
            current = current.next
        print("##############")
        print()


# testing
if __name__ == "__main__":
    llist = LinkedList()
    llist.insert("Pedro")
    llist.insert(21)
    llist.insert("Italo")
    llist.insert(22)
    llist.printList()

    llist.remove(21)
    llist.printList()

    print(llist.getSize())
