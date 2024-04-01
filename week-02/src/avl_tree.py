class TreeNode:
    """
    Node of an AVL Tree class.
    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    """
    AVL Tree class.
    """

    def __init__(self):
        self.root = None

    def _height(self, node: TreeNode) -> int:
        """
        Returns the height of the node.
        """
        if node is None:
            return 0
        return node.height

    def _balance_factor(self, node: TreeNode) -> int:
        """
        Calculates the balance factor of the node.
        """
        if node is None:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _left_rotate(self, z: TreeNode) -> TreeNode:
        """
        Performs a left rotation on the given node.
        """
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._height(z.left), self._height(z.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))

        return y

    def _right_rotate(self, z: TreeNode) -> TreeNode:
        """
        Performs a right rotation on the given node.
        """
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self._height(z.left), self._height(z.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))

        return y

    def _balance(self, node: TreeNode) -> TreeNode:
        """
        Balances the AVL tree starting from the given node.
        """
        if node is None:
            return node

        node.height = 1 + max(self._height(node.left), self._height(node.right))

        balance = self._balance_factor(node)

        if balance > 1:
            if self._balance_factor(node.left) < 0:
                node.left = self._left_rotate(node.left)
            return self._right_rotate(node)

        if balance < -1:
            if self._balance_factor(node.right) > 0:
                node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def _search_element(self, node: TreeNode, value: any) -> bool:
        """
        Searches for an element in the AVL tree.
        """
        if node is None:
            return False

        if node.value == value:
            return True
        elif value < node.value:
            return self._search_element(node.left, value)
        else:
            return self._search_element(node.right, value)

    def contains(self, value: any) -> bool:
        """
        Public method to check if an element is present in the AVL tree.
        """
        return self._search_element(self.root, value)

    def _add(self, node: TreeNode, value: any) -> TreeNode:
        """
        Adds a value to the AVL tree.
        """
        if node is None:
            return TreeNode(value)
        elif value < node.value:
            node.left = self._add(node.left, value)
        else:
            node.right = self._add(node.right, value)

        return self._balance(node)

    def add(self, value: any):
        """
        Public method to add a value to the AVL tree.
        """
        if self.contains(value):
            return
        self.root = self._add(self.root, value)

    def _search_prefix(self, node: TreeNode, prefix: str, results: list):
        """
        Searches for words with the given prefix starting from the specified node.
        """
        if node is None:
            return

        if node.value.startswith(prefix):
            results.append(node.value)

        if node.value >= prefix:
            self._search_prefix(node.left, prefix, results)

        self._search_prefix(node.right, prefix, results)

    def words_with_prefix(self, prefix: str) -> list:
        """
        Finds all words in the AVL tree that start with the given prefix.
        """
        results = []
        self._search_prefix(self.root, prefix, results)
        return results
