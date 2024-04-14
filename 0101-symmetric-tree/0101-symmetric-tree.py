# Definition for a binary tree node.
def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        if root is None:
            return True

        return self.isMirror(root.left, root.right)
    # I was not using self due to which so many errors occured. :)) Don't be silly, don't repeat my mistake
    def isMirror(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None or left.val != right.val:
            return False
        return self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)    