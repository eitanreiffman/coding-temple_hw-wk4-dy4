class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return self.value

    def __repr__(self):
        return f"<{self.value}>"

class LinkedList:
    def __init__(self):
        self.head = None

    # Method that will return a node based on value, or return None if it doesn't exist
    def _get_node(self, value_to_get):
        # Start with the first node in our Linked List
        node_to_check = self.head
        while node_to_check is not None:
            # If the value of the node is equal to the value to get
            if node_to_check.value == value_to_get:
                # Return that node
                return node_to_check
            # if not, move on to the next node
            node_to_check = node_to_check.next
        # If the value to get isn't found, we return None
        return None

    # Method to add a new value to the front of a Linked List
    def push_on(self, new_value):
        #Create new node with the value
        new_node = Node(new_value)
        # Set the next value for our new beginning node to our old beginning node
        new_node.next = self.head
        # Set the new node to be the front of the head
        self.head = new_node

    # Method to add to the end of our Linked List
    def append(self, new_value):
        # Create a new node with the value
        new_node = Node(new_value)
        # Checked if list is empty
        if self.head is None:
            # Set head to new node
            self.head = new_node
        # If it's not empty
        else:
            # Traverse to the end of the list (AKA the node.next is None)
            node = self.head
            # While the node has a .next attribute
            while node.next is not None:
                # Move on to the next node
                node = node.next
            # Set the last node's next attribute to be the new node
            node.next = new_node

    # Method to insert a node to our linked list after a certain node (by value)
    def insert_after(self, prev_value, new_value):
        # Get the previous node by its value
        prev_node = self._get_node(prev_value)
        # Check if previous node exists
        if prev_node is None:
            print(f"{prev_value} is not in linked list.")
            return None
        # Create a new node with the new value
        new_node = Node(new_value)
        # Point new node's next to the previous node's next
        new_node.next = prev_node.next
        # And point previous node's next to our new node
        prev_node.next = new_node


    # Method to print all items of Linked List
    def traverse_list(self):
        # Start at the beginning of the linked list
        node = self.head
        # While the node is not a 'None' type, AKA the last node, continue to loop
        while node is not None:
            # Print node, calls the node class' __str__ method
            print(node)
            # Set node to the next node in the linked list
            node = node.next

    # Above are notes from class. Below is the Remove Method that was added for the Homework Exercise

    # Method to remove a node value from the Linked List
    def remove_node(self, value_to_remove):
        # Start at the beginning of the list
        node = self.head
        if node is not None:
            if node.value == value_to_remove:
                self.head = node.next
                node = None
                return

        while node is not None:
            if node.value == value_to_remove:
                break
            prev = node
            node = node.next

        prev.next = node.next
        node = None



weekdays = LinkedList()
weekdays.push_on("Wednesday")
weekdays.push_on("Monday")
weekdays.append("Thursday")
weekdays.append("Friday")
weekdays.insert_after("Monday", "Tuesday")
weekdays.push_on("Sunday")
weekdays.append("Saturday")
print("All the days of the week:")
weekdays.traverse_list()
print("=============")

print("List After Deletion of 'Wednesday' and 'Saturday'")
weekdays.remove_node("Wednesday")
weekdays.remove_node("Saturday")
weekdays.traverse_list()