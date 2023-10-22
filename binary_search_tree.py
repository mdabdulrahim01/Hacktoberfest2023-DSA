class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if node is None:
            return TreeNode(key)
        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
        else:
            node.right = self._insert_recursive(node.right, key)
        return node

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)

# Create an empty BST
bst = BinarySearchTree()

# Get user input for inserting elements
while True:
    user_input = input("Enter an element to insert (or 'done' to finish): ")
    if user_input.lower() == 'done':
        break
    try:
        key = int(user_input)
        bst.insert(key)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Display the inorder traversal of the BST
print("Inorder traversal of the BST:")
print(bst.inorder_traversal())

# Get user input for searching for an element
search_input = input("Enter an element to search for: ")
try:
    search_key = int(search_input)
    result = bst.search(search_key)
    if result:
        print(f"Key {search_key} found in the BST.")
    else:
        print(f"Key {search_key} not found in the BST.")
except ValueError:
    print("Invalid input. Please enter a valid integer for search.")
