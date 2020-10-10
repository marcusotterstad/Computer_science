from nodes import Node

class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)
    
    #returnerer head Node i linked listen
    def get_head_node(self):
        return self.head_node
  
    #inserter en Node i slutten av linked listen
    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node
    
    #traverser gjennom alle Nodes og legger til hver value i en string, returnerer stringen
    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() != None:
                string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string_list

    #traverser gjennom alle Nodes til den finner valuen å fjerne, og setter forrige Node sin link til Noden etter. Returnerer Noden sin value
    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else:
                    current_node = next_node
