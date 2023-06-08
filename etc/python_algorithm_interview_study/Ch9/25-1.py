# https://leetcode.com/problems/design-circular-queue/
# 75ms 14.7MB
class MyCircularQueue:
    def __init__(self, k: int):
        self.circle_queue = [None] * k
        self.length = k
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        # 뒤가 비었으면 들어갈수 있다
        if self.circle_queue[self.rear] is None:
            self.circle_queue[self.rear] = value
            self.rear = (self.rear + 1) % self.length
            return True
        else:
            return False

    def deQueue(self) -> bool:
        # 앞이 비었으면 빈상태
        if self.circle_queue[self.front] is None:
            return False
        else:
            self.circle_queue[self.front] = None
            self.front = (self.front + 1) % self.length
            return True

    def Front(self) -> int:
        if self.circle_queue[self.front] is None:
            return -1
        else:
            return self.circle_queue[self.front]

    def Rear(self) -> int:
        if self.circle_queue[self.front] is None:
            return -1
        else:
            # self.rear은 None이다
            return self.circle_queue[self.rear - 1]

    def isEmpty(self) -> bool:
        # 원형큐의 초기상태
        return self.rear == self.front and self.circle_queue[self.rear] is None

    def isFull(self) -> bool:
        # 앞과 뒤가 같고 수가있으면 꽉찬 상태이다.
        return self.rear == self.front and self.circle_queue[self.rear] is not None