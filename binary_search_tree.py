class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.parent = None
        self.key = key
        self.value = None

    def __repr__(self):
        return f"({self.key}, {self.value})"

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # O(n) worse case, O(log n) average case, O(h) always
    def __contains__(self, key):
        current_node = self.root

        while current_node is not None:
            if key < current_node.key:
                current_node = current_node.left
            elif key > current_node.key:
                current_node = current_node.right
            else: 
                return True
        return False

    # O(n) linear time
    def __iter__(self):
        yield from self._in_order_traversal(self.root)

    # O(n)
    def __repr__(self):
        return str(list(self._in_order_traversal(self.root)))

    # O(n) worse case, O(log n) average case, O(h) always
    def insert(self, key, value):
        if self.root is None:
            self.root = Node(key)
            self.root.value = value
        else:
            current_node = self.root
            while True:
                if key < current_node.key:
                    if current_node.left is None:
                        current_node.left = Node(key)
                        current_node.left.value = value
                        current_node.left.parent = current_node
                        break
                    else:
                        current_node = current_node.left
                elif key > current_node.key:
                    if current_node.right in None:
                        current_node.right  = Node(key)
                        current_node.right.value = value
                        current_node.right.parent = current_node
                        break
                    else:
                        current_node = current_node.right
                else:
                    current_node.value = value
                    break

    # O(n) worse case, O(log n) average case, O(h) always
    def search(self, key):
        current_node = self.root

        while True:
            if current_node is None or current_node.key == key:
                return current_node
            elif key < current_node.key:
                if current_node.left is None:
                    return None
                else:
                    current_node = current_node.node.left
            else:
                if current_node.right is None:
                    return None
                else:
                    current_node = current_node.right

    # O(n) worse case, O(log n) average case, O(h) always
    def delete(self, key):
        node = self.search(key)

        if node is None:
            raise ValueError('Node with this key does not exist')

        self._delete(node)

    # O(n) linear time
    def traverse(self, order):
        if order == "inorder":
            yield from self._in_order_traversal(self.root)
        elif order == "preorder":
            yield from self._post_order_traversal(self.root)
        elif order == "postorder":
            yield from self._post_order_traversal(self.root)
        else:
            raise ValueError("Unknown order")

    def _delete(self, node):
        # Node is leaf node
        if node.left is None and node.right is None:
            if node.parent is None:
                self.root = None
            else:
                if node.parent.right == node:
                    node.parent.right = None
                else:
                    node.parent.left = None
                node.parent = None

        elif node.left is None or node.right is None:
            child_node = node.left if node.left is not None else node.right

            if node.parent is None:
                child_node.parent = None
                self.root = child_node
            else:
                if node.parent.right == node:
                    node.parent.right = child_node
                else:
                    node.parent.left = child_node
                child_node.parent = node.parent

            node.parent = node.left = node.right = None
        else:
            successor = self._successor(node)

            node.key = successor.key
            node.value = successor.value

            self.delete(successor)

        # Node has one child
        # Node has two child

    def _successor(self, node):
        if node is None:
            raise ValueError("cannot find successor of None")

        if node.right is None:
            return None
        else:
            current_node = node.right
            while current_node.left is None:
                current_node = current_node.left
            return current_node

    def _predecessor(self, node):
        if node is None:
            raise ValueError('Cannot find predecessor of None')

        if node.left is None:
            return None
        else:
            current_node = node.left
            while current_node.right is not None:
                current_node = current_node.right
            return current_node

    def _in_order_traversal(self, node):
        if node is not None:
            yield from self._in_order_traversal(node.left)
            yield (node.key, node.value)
            yield from self._in_order_traversal(node.right)

    def _pre_order_traversal(self, node):
        if node is not None:
            yield (node.key, node.value)
            yield from self._pre_order_traversal(node.left)
            yield from self._pre_order_traversal(node.right)

    def _post_order_traversal(self, node):
        if node is not None:
            yield from self._post_order_traversal(node.left)
            yield from self._post_order_traversal(node.right)
            yield (node.key, node.value)


if __name__ == '__main__':
    bst = BinarySearchTree()

    bst.insert(10, 'hello')
    bst.insert(5, 'hello')
    bst.insert(22, 'hello')
    bst.insert(2, 'hello')
    bst.insert(9, 'hello')

    bst.insert(12, 'hello')
    bst.insert(30, 'hello')
    bst.insert(11, 'hello')
    bst.insert(15, 'hello')

    bst.insert(30, 'hello')
    bst.insert(23, 'hello')
    bst.insert(35, 'hello')

    for i in bst.traverse('inorder'):
        print(i)

#tree = BinarySearchTree()
#for i in tree:
#    pass