# https://leetcode.com/problems/design-hashmap/
# 256ms 17.4MB
import collections


class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    def put(self, key: int, value: int) -> None:
        index = key % self.size
        # 인덱스 빈 경우
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return
        # 연결 리스트 만들기
        p = self.table[index]
        while p:
            # 이미 존재하는키 업데이트
            if p.key == key:
                p.value = value
                return
            # 다음이 널값이면삽입
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = key % self.size
        # 노드 없을때
        if self.table[index].value is None:
            return -1
        # 키 일치할때 값 출력
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            return
        # 인덱스의 첫 번째 노드일 때 삭제 처리
        p = self.table[index]
        if p.key == key:
            if p.next is None:
                self.table[index] = ListNode()
            else:
                self.table[index] = p.next
            return
        # 연결 리스트 노드 삭제
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next