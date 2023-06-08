# https://leetcode.com/problems/design-circular-deque/
# 135ms 15MB
class Node:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next = next_node
        self.prev = prev_node


class MyCircularDeque:
    def __init__(self, k: int):
        self.head, self.tail = Node(None), Node(None)
        self.max_size = k
        self.size = 0
        self.head.next = self.tail
        self.tail.prev = self.head

    def insertFront(self, value: int) -> bool:
        if not self.isFull():
            new_node = Node(value)
            head_next = self.head.next
            self.head.next, head_next.prev = new_node, new_node
            new_node.prev, new_node.next = self.head, head_next
            self.size = self.size + 1
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if not self.isFull():
            new_node = Node(value)
            tail_prev = self.tail.prev
            self.tail.prev, tail_prev.next = new_node, new_node
            new_node.next, new_node.prev = self.tail, tail_prev
            self.size = self.size + 1
            return True
        return False

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        else:
            head_next = self.head.next.next
            head_next.prev, self.head.next = self.head, head_next
            self.size = self.size - 1
            return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        else:
            tail_prev = self.tail.prev.prev
            tail_prev.next, self.tail.prev = self.tail, tail_prev
            self.size = self.size - 1
            return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.head.next.value

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.tail.prev.value

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max_size