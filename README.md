studying linked



# Conclusion: Stack (Data Structure)
A Stack is a linear data structure that follows LIFO (Last In, First Out).

Think of a pile of plates: the last plate you put on top is the first plate you remove.

# Conclusion: Queue (Data Structure)
**Technical conclusion:**

A Queue is a linear data structure that follows the First In, First Out (FIFO) principle. Your implementation uses a singly linked list with front and rear pointers to efficiently manage insertion and removal.

# Conclusion: Hash map (Data Structure)
**Technical explanation: HashMap**

**Hash map is very important data structure**
A HashMap is a data structure that stores information in key-value pairs.

Each piece of information has two parts:
- Key: Used to identify or find the data.
- Value: The actual data associated with that key.



** The Law of Large Numbers **
The Law of Large Numbers is a statistical principle stating that as the number of independent observations or experiments increases, the sample average tends to converge toward the true expected value. In other words, collecting more observations generally makes the results more representative of the actual average or probability, provided the data meets the necessary statistical assumptions.

Imagine flipping a coin. You know that a coin has a 50% chance of landing on heads and a 50% chance of landing on tails. If you flip it only 10 times, you might get 7 heads and 3 tails. But if you flip it 10,000 times, the results will generally get closer to 50% heads and 50% tails. That's the Law of Large Numbers: the more times you repeat something, the closer your average results tend to get to what you would normally expect.


# Conclusion: Binary Search Tree (Data Structure)
**Technical explanation: binary search tree**

A Binary Search Tree is a hierarchical data structure that stores elements in an ordered manner. Each node contains a key and can have at most two children: a left child containing smaller keys and a right child containing larger keys. This structure allows searching, insertion, and deletion to operate in O(log n) time on average when the tree is reasonably balanced. However, an unbalanced BST can degrade to O(n) time complexity. BSTs also support different traversal techniques, such as in-order, pre-order, and post-order traversal.

A Binary Search Tree is like organizing numbers in a family tree. Every number has a place, and the rule is that smaller numbers go to the left while bigger numbers go to the right. This makes finding, adding, and removing numbers easier because you don't need to check every number one by one. However, if the tree becomes unbalanced, finding numbers can become slower.



# Conclusion: Heap (Data Structure)

A Heap is a tree-based data structure, typically implemented using an array, that maintains a specific ordering property. A Min Heap ensures that every parent node is smaller than or equal to its children, keeping the minimum element at the root. Its main advantage is efficient insertion and removal of the minimum element, both taking O(log n) time, while accessing the minimum takes O(1). Heaps are commonly used to implement priority queues and are useful in scheduling, graph algorithms, and other applications that require efficient priority-based processing.


A Heap is like a pyramid where the smallest number stays at the top. Whenever you add a new number, it moves upward if it's smaller than its parent. Whenever you remove the smallest number, another number takes its place and moves down until everything is organized again. This makes it easy to find the smallest number without sorting everything.