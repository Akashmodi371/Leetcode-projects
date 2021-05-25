class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist():
    def __int__(self):
        self.head=None

    def printlinkedlist(self):
        temp = self.head
        while (temp):
            print(temp.data, end="->")
            temp = temp.next


list1=linkedlist()
list1.head=Node(2)
second1=Node(4)
third1=Node(3)

list2=linkedlist()
list2.head=Node(5)
second2=Node(6)
third2=Node(4)

list1.printlinkedlist()
    # list2.printlinkedlist()