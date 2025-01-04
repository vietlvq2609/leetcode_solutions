from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # Recursive solution
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)
        return [*left, root.val, *right]

    # Iterative solution
    def inorderTraversalIterative(self, root: Optional[TreeNode]) -> List[int]:
        result = []  # List to store the traversal result
        stack = []   # Stack to simulate the recursive call stack
        current = root  # Start with the root node

        while current is not None or stack:
            # Reach the leftmost node of the current subtree
            while current is not None:
                stack.append(current)  # Push the current node onto the stack
                current = current.left  # Move to the left child

            # Pop the top node from the stack
            current = stack.pop()
            result.append(current.val)  # Process the current node

            # Move to the right subtree
            current = current.right

        return result

solution = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(8)
root.right.right.left = TreeNode(6)
root.right.right.right = TreeNode(7)
root.right.right.left.right = TreeNode(9)
print(solution.inorderTraversalIterative(root))  # Output: [4, 2, 5, 1, 3, 6, 9, 8, 7]