class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def insert_begin(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			return
		else:
			new_node.next = self.head
			self.head = new_node

	def insert_index(self, data, index):
		new_node = Node(data)
		current_node = self.head
		position = 0
		if position == index:
			self.insert_begin(data)
		else:
			while(current_node != None and position+1 != index):
				position += 1
				current_node = current_node.next

			if current_node != None:
				new_node.next = current_node.next
				current_node.next = new_node
			else:
				print("Index not present")

	def insert_end(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			return
		current_node = self.head
		while(current_node.next):
			current_node = current_node.next

		current_node.next = new_node

	def update_node(self, val, index):
		current_node = self.head
		position = 0
		if position == index:
			current_node.data = val
		else:
			while(current_node != None and position != index):
				position += 1
				current_node = current_node.next
			if current_node != None:
				current_node.data = val
			else:
				print("Index not present")

	def remove_first_node(self):
		if(self.head == None):
			return
		self.head = self.head.next

	def remove_last_node(self):
		if self.head is None:
			return
		current_node = self.head
		while(current_node.next.next):
			current_node = current_node.next
		current_node.next = None

	def remove_at_index(self, index):
		if self.head == None:
			return
		current_node = self.head
		position = 0
		if position == index:
			self.remove_first_node()
		else:
			while(current_node != None and position+1 != index):
				position += 1
				current_node = current_node.next
			if current_node != None:
				current_node.next = current_node.next.next
			else:
				print("Index not present")

	def remove_node(self, data):
		current_node = self.head
		while(current_node != None and current_node.next.data != data):
			current_node = current_node.next
		if current_node == None:
			return
		else:
			current_node.next = current_node.next.next

	def size_linked_list(self):
		size = 0
		if(self.head):
			current_node = self.head
			while(current_node):
				size += 1
				current_node = current_node.next
			return size
		else:
			return 0

	def print_linked_list(self):
		current_node = self.head
		while(current_node):
			print(current_node.data)
			current_node = current_node.next


# create a new linked list
llist = LinkedList()

# add nodes to the linked list
llist.insert_end('a')
llist.insert_end('b')
llist.insert_begin('c')
llist.insert_end('d')
llist.insert_index('g', 2)

print("\nNode Data")
llist.print_linked_list()

print("\nRemove First Node")
llist.remove_first_node()
llist.print_linked_list()

print("\nRemove Last Node")
llist.remove_last_node()
llist.print_linked_list()

print("\nRemove Node at Index 1")
llist.remove_at_index(1)
llist.print_linked_list()


print("\nUpdate node 0 Value")
llist.update_node('z', 0)
llist.print_linked_list()

print("\nSize of linked list :", end=" ")
print(llist.size_linked_list())
