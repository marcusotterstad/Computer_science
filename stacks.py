from nodes import Node

class Stack:
    def __init__(self, limit=1000):
        self.top_item = None
        self.size = 0
        self.limit = limit
  
    #legger til en Node øverst i stacken
    def push(self, value):
        if self.has_space():
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            self.size += 1
            print("Adding {} to the stack!".format(value))
        else:
            print("No room for {}!".format(value))

    #fjerner den øverste Noden og returnerer verdien til Noden som ble fjernet
    def pop(self):
        if not self.is_empty():
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1
            print("Delivering " + item_to_remove.get_value())
            return item_to_remove.get_value()
        print("No more items.")

    #returnerer verdien til den øverste noden
    def peek(self):
        if not self.is_empty():
            return self.top_item.get_value()
        print("Nothing to see here!")

    #returnerer en boolean om stacken har plass
    def has_space(self):
        return self.limit > self.size

    #returnerer en boolean om stacken er tom
    def is_empty(self):
        return self.size == 0