# why it's a bad idea to use lists for queues
#https://docs.python.org/3.1/tutorial/datastructures.html#using-lists-as-queues
# collections.deque is actually a linked list https://wiki.python.org/moin/TimeComplexity


# queue looks like:
#d<-c<-b<-a
# where a is the frontmost node
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

    def __str__(self):
    	return str(self.data)


class queue:

	def __init__(self):
		self.front = None
		self.back = None
		self.length = 0

	def __str__(self):
		mynode = self.front
		a = str(mynode)
		while mynode:
			mynode = mynode.next
			a = str(mynode)+"<-"+a
		return a

	def add(self, data):
		if self.front is None:
			newnode = Node(data)
			self.front = self.back = newnode
		else:
			newnode = Node(data)
			self.back.next = newnode
			self.back = newnode
		self.length += 1

	def remove(self):
		if self.length<=1:
			tmpnode = self.front
			self.front = None
			self.back = None
		else:
			tmpnode = self.front
			self.front = tmpnode.next
		self.length -= 1
		return tmpnode



a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

Q = queue()
print(Q.front)
print(Q.back)
Q.add("a")
print(Q.front)
print(Q.back)
Q.add("b")
print(Q.front)
print(Q.back)
Q.add("c")
print(Q.front)
print(Q.back)
Q.add("d")
print(Q.front)
print(Q.back)

print(Q)


print(Q.front)
print(Q.back)
Q.remove()
print(Q.front)
print(Q.back)
Q.remove()
print(Q.front)
print(Q.back)
print(Q)
Q.remove()
print(Q.front)
print(Q.back)
Q.remove()
print(Q.front)
print(Q.back)


print(Q)



