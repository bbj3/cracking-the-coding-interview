import unittest
# not nice to use pop(0) for lists when implementing a queue, see
# https://docs.python.org/3/library/collections.html#collections.deque

class Node():
    def __init__(self, data, adjacency_list=None):
        self.data = data
        self.adjacency_list = adjacency_list or []
        self.marked = False
  
    def add_edge_to(self, node):
        self.adjacency_list += [node]

    def __str__(self):
        return self.data

class Queue():
    def __init__(self):
        self.array = []
  
    def add(self, item):
        self.array.append(item)
  
    def remove(self):
        if not len(self.array):
            return None
        item = self.array[0]
        del self.array[0]
        return item

    def isempty(self):
        if (len(self.array)==0):
            return True
        else:
            return False

def visitcheck(Node1, Node2):
    if Node1==Node2:
        return True
    else:
        return False

def breadthfirst(Node1, Node2):
    Node1.marked = True
    tmp_queue = Queue()
    tmp_queue.add(Node1)
    cnt = 0
    while(not tmp_queue.isempty()):
        tmp_node = tmp_queue.remove()
        found = visitcheck(tmp_node, Node2)
        if found:
            return True
        tmp_adjacent_nodes = tmp_node.adjacency_list
        for neighbornode in tmp_adjacent_nodes:
            if (neighbornode.marked==False):
                neighbornode.marked=True
                tmp_queue.add(neighbornode)
        cnt=cnt+1
    return False

# for testing we have to create all nodes 3 times so we forget that we have visited them before
class Test(unittest.TestCase):
    def test_find_route(self):
        node_j = Node('J')
        node_i = Node('I')
        node_h = Node('H')
        node_d = Node('D')
        node_f = Node('F', [node_i])
        node_b = Node('B', [node_j])
        node_g = Node('G', [node_d, node_h])
        node_c = Node('C', [node_g])
        node_a = Node('A', [node_b, node_c, node_d])
        node_e = Node('E', [node_f, node_a])
        node_d.add_edge_to(node_a)
        self.assertEqual(breadthfirst(node_a, node_i), False)
        print("list")
        node_j = Node('J')
        node_i = Node('I')
        node_h = Node('H')
        node_d = Node('D')
        node_f = Node('F', [node_i])
        node_b = Node('B', [node_j])
        node_g = Node('G', [node_d, node_h])
        node_c = Node('C', [node_g])
        node_a = Node('A', [node_b, node_c, node_d])
        node_e = Node('E', [node_f, node_a])
        node_d.add_edge_to(node_a)
        self.assertEqual(breadthfirst(node_a, node_j), True)
        node_j = Node('J')
        node_i = Node('I')
        node_h = Node('H')
        node_d = Node('D')
        node_f = Node('F', [node_i])
        node_b = Node('B', [node_j])
        node_g = Node('G', [node_d, node_h])
        node_c = Node('C', [node_g])
        node_a = Node('A', [node_b, node_c, node_d])
        node_e = Node('E', [node_f, node_a])
        node_d.add_edge_to(node_a)
        node_h.add_edge_to(node_i)

        self.assertEqual(breadthfirst(node_a, node_i), True)

if __name__ == "__main__":
    unittest.main()







