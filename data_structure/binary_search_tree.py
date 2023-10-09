class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)

        if self.root == None:
            self.root = new_node
            return self

        current = self.root
        while(True):
            if current.value > value:
                if current.left == None:
                    current.left = new_node
                    return self
                current = current.left
            elif current.value < value:
                if current.right == None:
                    current.right = new_node
                    return self
                current = current.right
            else:
               raise Exception(f'There is an exist node with value {value}')
    
    def find(self, value):
        current = self.root

        while(True):
            if current == None:
                return False

            if current.value > value:
                current = current.left
            elif current.value < value:
                current = current.right
            else:
                return current

        
data = BinarySearchTree()
data.insert(10)
data.insert(5)
data.insert(12)
data.insert(15)
data.insert(3)
print(data.find(3))
print(data.find(2))
