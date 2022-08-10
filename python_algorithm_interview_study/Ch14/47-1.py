# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# 220ms 20.1MB
import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    @staticmethod
    def serialize(root):
        q = collections.deque([root])
        result = ['#']
        while q:
            node = q.popleft()
            # 트리에 값이 있으면 값을 넣고 없으면 '#'을 넣는다.
            if node:
                result.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                result.append('#')
        return ' '.join(result)

    @staticmethod
    def deserialize(data):
        if data == '# #':
            return None
        nodes = data.split()
        # 루트노드
        root = TreeNode(nodes[1])
        q = collections.deque([root])
        idx = 2
        while q:
            node = q.popleft()
            if nodes[idx] != '#':
                node.left = TreeNode(int(nodes[idx]))
                q.append(node.left)
            idx += 1
            if nodes[idx] != '#':
                node.right = TreeNode(int(nodes[idx]))
                q.append(node.right)
            idx += 1
        return root