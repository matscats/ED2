class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


class BinaryTree:
    def __init__(self):
        self.root = None

    def _add(self, current_node, key):
        """
        Adds a value to the Binary tree.
        """
        if key < current_node.key:
            if current_node.left is None:
                current_node.left = TreeNode(key)
            else:
                self._add(current_node.left, key)
        elif key > current_node.key:
            if current_node.right is None:
                current_node.right = TreeNode(key)
            else:
                self._add(current_node.right, key)

    def add(self, key):
        """
        Public method to add a value to the Binary tree.
        """
        if not self.root:
            self.root = TreeNode(key)
        else:
            self._add(self.root, key)

    def contains(self, value: any) -> bool:
        """
        Public method to check if an element is present in the Binary tree.
        """
        return self._search_element(self.root, value)

    def _search_element(self, node: TreeNode, value: any) -> bool:
        """
        Searches for an element in the Binary tree.
        """
        if node is None:
            return False

        if node.value == value:
            return True
        elif value < node.value:
            return self._search_element(node.left, value)
        else:
            return self._search_element(node.right, value)

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
