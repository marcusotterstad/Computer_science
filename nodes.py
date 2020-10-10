### Node Class ###

class Node:
    def __init__(self, value, link_node=None):
        self.value = value  #verdien til Noden
        self.link_node = link_node  #link til neste Node

    #setter neste Node
    def set_next_node(self, link_node):
        self.link_node = link_node

    #returnerer neste Node
    def get_link_node(self):
        return self.link_node

    #henter verdien til Node
    def get_value(self):
        return self.value

