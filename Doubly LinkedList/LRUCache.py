# from collections import OrderedDict

# class LRUCache:

#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.container = OrderedDict()
        

#     def get(self, key: int) -> int:
#         val = self.container.get(key)
#         if val:
#             self.container.move_to_end(key)
#             return val
#         return -1
        

#     def put(self, key: int, value: int) -> None:
#         if key in self.container:
#             self.container.move_to_end(key)
#         if len(self.container) == self.capacity:
#             self.container.popitem(last=False)
#         self.container[key] = value

class ListNode:
    def __init__(self, key, val, prev=None, next=None) -> None:
        self.key = key 
        self.val = val
        self.prev = prev
        self.next = next 


class DLL:
    def __init__(self):
        dummy = ListNode(-1, -1)
        self.head = dummy
        self.tail = dummy

    def insert_from_end(self, node):
        self.tail.next = node
        node.prev = self.tail
        node.next = None
        self.tail = node


    def delete_from_start(self):
        self.head.next = self.head.next.next
        if self.head.next:
            self.head.next.prev = self.head
        else:
            self.tail = self.head

    def move_to_end(self, node):
        if node.next:
            next = node.next
            prev = node.prev

            prev.next = next
            next.prev = prev

            self.insert_from_end(node)


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.container = {}
        self.tracker = DLL()

    def get(self, key: int) -> int:
        if key in self.container:
            node = self.container[key]
            self.tracker.move_to_end(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.container:
            node = self.container[key]
            self.tracker.move_to_end(node)
            self.container[key].val = value
        elif len(self.container) == self.capacity:
            node = self.tracker.head.next
            self.container.pop(node.key)
            self.tracker.delete_from_start()

            new_node = ListNode(key, value)
            self.container[key] = new_node
            self.tracker.insert_from_end(new_node)
        else:
            new_node = ListNode(key, value)
            self.container[key] = new_node
            self.tracker.insert_from_end(new_node)