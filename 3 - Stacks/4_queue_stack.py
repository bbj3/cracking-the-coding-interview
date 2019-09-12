# we simply have two stacks - one being the main stack and the other we use for temporary use when removeing an element from the queue
class QueueStack():
    def __init__(self):
        self.stack = StackLL()
        self.tempstack = StackLL()

    def Add2Q(self,data):
        self.stack.push(data)

    def removefromQ(self):
        while not(self.stack.isitempty()): # all elements in stack on to tempstack 
            popping=self.stack.pop()
            self.tempstack.push(popping)
        queuelement = self.tempstack.pop()
        while not(self.tempstack.isempty()): # all elements in tempstack back to the original stack
            popping=self.tempstack.pop()
            self.push(popping)
        return queuelement

    def __str__(self):
        return(str(self.tempstack))





class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

    def __str__(self):
        return(str(self.data))


class StackLL:
    
    def __init__(self):
        self.top=None
        self.cnt=0

    def __str__(self):
        mynode  = self.top
        if mynode==None:
            return("None")
        mynodestr = str(mynode.data)
        while mynode.next:
            mynodestr = str(mynode.next.data)+"<-"+mynodestr
            mynode = mynode.next
        return(mynodestr)

    def push(self,data):
        newnode=Node(data)
        newnode.next=self.top
        self.top=newnode
        self.cnt=self.cnt+1

    def pop(self):
        if (self.isitempty()):
            return None
        temp=self.top
        self.top=self.top.next
        popped=temp.data
        self.cnt=self.cnt-1
        return temp

    def isitempty(self):
        if (self.top is None):
            return True 
        else:
            return False
    def peek(self):
        return self.top.data


import unittest

class TestStringMethods(unittest.TestCase):

    def test_queue_stack(self):

        sll = StackLL()
        sll.push(1)
        self.assertEqual(str(sll), "1")
        sll.push(2)
        self.assertEqual(str(sll), "1<-2")
        sll.push(3)
        self.assertEqual(str(sll), "1<-2<-3")
        sll.push(4)
        sll.push(5)
        self.assertEqual(str(sll), "1<-2<-3<-4<-5")
        self.assertEqual(str(sll.pop()), "5")
        self.assertEqual(str(sll.pop()), "4")

        self.assertEqual(str(sll), "1<-2<-3")
        sll.pop()
        sll.pop()

        self.assertEqual(str(sll.pop()), "1")
        self.assertEqual(str(sll.pop()), "None")
        


if __name__ == '__main__':
    unittest.main()




