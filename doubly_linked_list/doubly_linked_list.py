"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

"""
Our doubly-linked list class. It holds references to
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):

        if self.head is None:
            node = ListNode(value)
            self.head = node
            self.tail = node
        elif self.head == self.tail:
            node = ListNode(value=value, prev=None, next=self.head)
            self.head = node
            self.tail = node.next
        else:
            node = ListNode(value=value, prev=None, next=self.head)
            self.head = node
        self.length += 1
        return self

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head == self.tail:
            removed = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return removed
        else:
            removed = self.head.value
            new_head = self.head.next
            self.head = None
            self.head = new_head
            self.length -= 1
            return removed

    """
    Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        if self.tail is None:
            node = ListNode(value)
            self.head = node
            self.tail = node
        elif self.head == self.tail:
            node = ListNode(value=value, prev=self.head, next=None)
            self.head = node.prev
            self.tail = node
        else:
            node = ListNode(value=value, prev=self.tail, next=None)
            self.tail = node
        self.length += 1
        return self

    """
    Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.head == self.tail:
            removed = self.tail.value
            self.head = None
            self.tail = None
            self.length -= 1
            return removed
        else:
            removed = self.tail.value
            new_tail = self.tail.prev
            self.tail = None
            self.tail = new_tail
            self.length -= 1
            return removed

    """
    Removes the input node from its current spot in the
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):

        pass

    """
    Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the
    order of the other elements of the List.
    """
    def delete(self, node):
        if node is None or self is None:
            return None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node = None
            self.length -= 1
            return self


    """
    Finds and returns the maximum value of all the nodes
    in the List.
    """
    def get_max(self):
        if self.head is None:
            return None
        cur_node = self.head
        cur_max = cur_node.value
        while cur_node is not None:
            if cur_node.value > cur_max:
                cur_max = cur_node.value
            cur_node = cur_node.next
        return cur_max
