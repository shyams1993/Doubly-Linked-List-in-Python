class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        return str(self.__dict__)

    def printDLL(self):
        currentNode = self.head
        lis = []
        while currentNode != None:
            lis.append(currentNode.data)
            currentNode = currentNode.next
        return lis

    def append(self,data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            self.tail = self.head
            self.length += 1
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
            self.length+=1

    def prepend(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode
        self.length += 1

    def insert(self,index,data):
        newNode = Node(data)
        currentNode = self.head
        if index == 0:
            self.prepend(newNode.data)
        elif index == self.length:
            self.append(newNode.data)
        else:
            i= 0
            while i < self.length:
                if i == index - 1:
                    newNode.next = currentNode.next
                    currentNode.next = newNode
                    newNode.prev = currentNode
                    currentNode.next.next.prev = newNode
                    self.length+=1
                currentNode = currentNode.next
                i+=1

    def remove(self,index):
        currentNode = self.head
        if index == 0:
            self.head = currentNode.next
            currentNode.prev = None
            self.length -= 1
        elif index == self.length-1:
            currentNode = self.tail.prev
            self.tail = currentNode
            currentNode.next = None
            self.length -= 1
        else:
            i = 0
            while i < self.length:
                if i == index - 1:
                    currentNode.next.next.prev = currentNode
                    currentNode.next = currentNode.next.next
                    self.length -= 1
                    break
                currentNode = currentNode.next
                i += 1

    def reverse(self):
        first = self.head
        self.tail = self.head
        second = first.next
        while second != None:
            third = second.next
            second.next = first
            second.prev = third
            first.prev = second
            first = second
            second = third
        self.head.next = None
        self.head = first



m = DoublyLinkedList()
m.append(100)
m.append(101)
m.append(102)
m.append(104)
m.append(105)
m.prepend(99)
m.insert(0,98)
m.insert(7,106)
m.insert(5,103)
m.remove(0)
m.remove(7)
m.insert(4,1000)
m.remove(4)
print(m)
print(m.reverse())
print(m.printDLL())