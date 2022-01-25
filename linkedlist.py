class LinkedList:
    def __init__(self, first=None):
        self.first = first
    def printList(self):
        current = self.first
        lista = []
        while current != None:
            if len(lista) == 0:
                lista.append(str(current.value))
                current = current.next
            else:
                lista.append('>'+str(current.value))
                current = current.next
        print(''.join(lista))


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

ll = LinkedList(node1)
ll.printList()

