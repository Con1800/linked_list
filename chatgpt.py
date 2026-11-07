class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class DoublylinkedList:
    def __init__(self):
        self.head = None
        # self.size = 0
        self.tail = None
        

    # O(n) lineat time
    def __repr__(self):
        if self.head is None:
            return "[]"
        else:
            last = self.head

            return_string = f"[{last.value}]"

            while last.next:
                last = last.next
                return_string += f", {last.value}"
            return_string += "]"

            return return_string

    # O(n) - linear time
    def __contains__(self, value):
        last = self.head
        while last is not None:
            if last.value == value:
                return True
            last = last.next
        return False

    # O(n) linear time
    def __len__(self):
        last = self.head
        counter = 0
        while last is not None:
            counter +=1
            last = last.next
        return counter

    # O(1) constants time
    def append(self, value):
            if self.head is None:
                self.head = Node(value)
                self.tail = self.head

            else:
                last_node = Node(value)
                last_node.previous = self.tail
                self.tail.next = last_node
                self.tail = last_node


    def prepend(self, value):
            first_node = Node(value)

            if self.head is None:
                self.head = first_node
                self.tail = first_node
            else:
                first_node.next = self.head
                self.head.previous = first_node
                self.head = first_node

    # O(n) - linear time
    def insert(self, value, index):
        if index < 0:
            raise ValueError("index out of bounds")
        
        if index == 0:
            self.prepend(value)
            return
        last = self.head

        for i in range(index - 1):
            if last is None:
                raise ValueError("index out of bounds")
            last = last.next

        if last is None:
            raise ValueError("Index out of bounds")

        new_node = Node(value)

        new_node.next = last.next
        new_node.previous = last

        if last.next is not None:
            last.next.previous = new_node
        else:
            self.tail = new_node
        last.next = new_node

    # O(n) linear time      
    def delete(self, value):
        last = self.head

        while last is not None:
            if last.value == value:

                if last.previous is not None:
                    last.previous.next = last.next
                else:
                    self.head = last.next

                if last.next is not None:
                    last.next.previous = last.previous
                else:
                    self.tail = last.previous

                return
            last = last.next

        if last is not None:
            if last.value == value:
                self.head = last.next
            else:
                while last.next:
                    if last.next.value == value:
                        last.next.next.previous = last
                        last.next = last.next.next
                        break
                    last = last.next

    

    def pop(self, index):
        if index < 0 or self.head is None:
            raise ValueError("Index out of bounds")

        last = self.head

        for i in range(index):
            if last is None:
                raise ValueError("Index is out of bounds")
            last = last.next

        if last is None:
            raise ValueError("Index out of bounds")

        if last.previous is not None:
            last.previous.next = last.next
        else:
            self.head = last.next

        if last.next is not None:
            last.next.previous = last.previous

        else:
            self.tail = last.previous

        return last.value
        
        

    # O(n) linear time
    def get(self, index):
        if self.head is None:
            raise ValueError("Index out of bounds")
        else:
            last = self.head
            for i in range(index):
                if last.next is None:
                    raise ValueError("Index out of bounds")
                last = last.next
            return last.value

    #def print(self):
        # pass

if __name__ == "__main__":
    ll = DoublylinkedList()

    ll.append(10)
    ll.append(5)
    ll.append(18)
    ll.append(22)
    ll.append(29)


    ll.prepend(100)
    ll.insert(200, 1)

    ll.delete(18)

    ll.pop(1)
    print(ll)

    print(ll.get(1))

    print(29 in ll)
    print(800 in ll)