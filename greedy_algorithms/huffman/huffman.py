import heapq
import time
from collections import deque
from heapq import heappush, heappop


class TreeNode(object):
    def __init__(self, left, right):
        self.a = None
        self.p = None
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.p) + " " + str(self.a)

    def __lt__(self, other):
        return self.p < other.p

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = str(self.p) + " " + str(self.a)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = str(self.p) + " " + str(self.a)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = str(self.p) + " " + str(self.a)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = str(self.p) + " " + str(self.a)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


def encode_huffman_tree_using_heap(alphabet, p):
    heap = []
    heapq.heapify(heap)
    for element, freq in zip(alphabet, p):
        treeNode = TreeNode(None, None)
        treeNode.a = element
        treeNode.p = freq
        heappush(heap, treeNode)
    while len(heap) >= 2:
        t1 = heappop(heap)
        t2 = heappop(heap)
        t3 = TreeNode(t1, t2)
        t3.p = t3.left.p + t3.right.p
        heappush(heap, t3)
    return heappop(heap)


def pop_min_node_from_queue(deq1, deq2):
    if len(deq2) > 0:
        if deq1[0].p < deq2[0].p:
            return deq1.popleft()
        else:
            return deq2.popleft()
    return deq1.popleft()


def encode_huffman_tree_using_sort(alphabet, p):
    nodes = []
    for element, freq in zip(alphabet, p):
        treeNode = TreeNode(None, None)
        treeNode.a = element
        treeNode.p = freq
        nodes.append(treeNode)
    nodes.sort()
    deq = deque(nodes)
    deq2 = deque([])
    while len(deq) >= 2:
        t1 = pop_min_node_from_queue(deq, deq2)
        t2 = pop_min_node_from_queue(deq, deq2)
        t3 = TreeNode(t1, t2)
        t3.p = t3.left.p + t3.right.p
        deq2.append(t3)
    while len(deq2) >= 2:
        t1 = deq2.popleft()
        t2 = deq2.popleft()
        t3 = TreeNode(t1, t2)
        t3.p = t3.left.p + t3.right.p
        deq2.append(t3)
    return deq2.popleft()


def get_min_depth(node, depth):
    if node is not None:
        if not node.left and not node.right:
            return depth
        return min(get_min_depth(node.left, depth + 1), get_min_depth(node.right, depth + 1))


def get_max_depth(node, depth):
    if node is not None:
        if not node.left and not node.right:
            return depth
        return max(get_max_depth(node.left, depth + 1), get_max_depth(node.right, depth + 1))


def main():
    p_arr = []
    alphabet_arr = []
    f = open("../../challenge14.6.txt", "r")
    numOfCases = int(f.readline())
    for i in range(0, numOfCases):
        line = f.readline()
        job_data = line.rstrip()
        p_arr.append(int(line.rstrip()))
        alphabet_arr.append(None)

    start1 = time.time()
    tree1 = encode_huffman_tree_using_sort(alphabet_arr, p_arr)
    end1 = time.time()
    tree1.display()
    start2 = time.time()
    tree2 = encode_huffman_tree_using_heap(alphabet_arr, p_arr)
    end2 = time.time()
    tree2.display()
    print("Sort implementation elapsed for: " + str((end1 - start1) * 1000) + "ms")
    print("Heap implementation elapsed for: " + str((end2 - start2) * 1000) + "ms")
    print("Min length of a codeword is: " + str(get_min_depth(tree1, 0)))
    print("Max length of a codeword is: " + str(get_max_depth(tree1, 0)))

main()
