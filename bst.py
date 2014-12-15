#!/usr/bin/python
from structures import TreeNode
from collections import deque

def inorder(root):
    if not root: return None
    output = []
    st = deque()
    st.append(root)
    # track if the node has been visited before
    visited = {}
    while st:
        node = st.pop()
        if node.left and not visited.get(node.left, False):
            st.append(node)
            st.append(node.left)
        else:
            output.append(node.val)
            visited[node] = True
            if node.right:
                st.append(node.right)
    return output

def minVal(node):
    if node.left: 
        return minVal(node.left)
    else: 
        return node

def findSucc(node, root):
    if node.right:
        return minVal(node.right)
    else:
        succ = root
        while succ:
            if root.val > node.val:
                succ = root
                root = root.left
            elif root.val < node.val:
                root = root.right
            else:
                break
        return succ

def delete(node, root):
    pass

t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t2.left = t1
t2.right = t3
print inorder(t2)
