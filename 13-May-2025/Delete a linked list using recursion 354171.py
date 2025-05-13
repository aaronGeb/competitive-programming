# Problem: Delete a linked list using recursion - https://www.geeksforgeeks.org/delete-linked-list-using-recursion/

class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

def delete_list(curr):

    # Base case: If the list is empty, return
    if curr is None:
        return
    delete_list(curr.next)

    curr = None

if __name__ == "__main__":

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    
    delete_list(head)
    head = None 
    print("Linked List deleted.")