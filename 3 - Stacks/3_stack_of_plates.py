# class which contains an array of linked lists, when one linked lists exceeds the capacity 
# we create a new linked list in the next place in the array.

"""[o->o->o->o->,o->o->o->o->,o->o->o->o->] is an example  stackofplates with capacity 4.
"""

class StackOfPlates:
    def __init__(self, capacity):
        self.stacks = []
        self.number_of_stacks = -1
        self.number_of_plates_in_latest_stack  = 0
        if capacity <1:
            raise NameError("stack is greater than 1")
        else:
            self.capacity=capacity


    def __str__(self):
        mystr = str(self.stacks[0])
        for mystack in self.stacks[1:]:
            mystr = mystr + "===" +str(mystack)
        return mystr

    def push(self, item):
        if self.number_of_plates_in_latest_stack%self.capacity==0:
            new_LL = StackLL()
            new_LL.push(item)
            self.stacks.append(new_LL)
            self.number_of_stacks = self.number_of_stacks+1
        else:
            self.stacks[self.number_of_stacks].push(item)
        self.update_number_of_plates_in_latest_stack()



    def pop(self):
        if self.stacks == []:
            raise NameError("can't pop empty stack")
        else:
            if self.number_of_plates_in_latest_stack == 1: # if the latest stack is biggger than capacity
                stack_on_top_of_list = self.stacks[self.number_of_stacks]
                popelem = stack_on_top_of_list.pop()
                del self.stacks[self.number_of_stacks]
                self.number_of_stacks = self.number_of_stacks-1
            else:
                popelem = self.stacks[self.number_of_stacks].pop()
        self.update_number_of_plates_in_latest_stack()
        return popelem

    def update_number_of_plates_in_latest_stack(self):
        if self.stacks != []:
            self.number_of_plates_in_latest_stack = self.stacks[self.number_of_stacks].cnt
        else:
            self.number_of_plates_in_latest_stack = 0



class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

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

    def test_plate_stack(self):

        sp = StackOfPlates(3)

        sp.push(3)
        self.assertEqual(str(sp), "3")
        sp.push(3)
        self.assertEqual(str(sp), "3<-3")
        sp.push(3)
        self.assertEqual(str(sp), "3<-3<-3")
        sp.push(3)
        self.assertEqual(str(sp), "3<-3<-3===3")        
        sp.push(5)
        self.assertEqual(str(sp), "3<-3<-3===3<-5")
        sp.push(6)
        self.assertEqual(str(sp), "3<-3<-3===3<-5<-6")
        sp.push(7)
        self.assertEqual(str(sp), "3<-3<-3===3<-5<-6===7")
        sp.push(8)
        self.assertEqual(str(sp), "3<-3<-3===3<-5<-6===7<-8")
        sp.pop()
        self.assertEqual(str(sp), "3<-3<-3===3<-5<-6===7")
        sp.pop()
        self.assertEqual(str(sp), "3<-3<-3===3<-5<-6")
        sp.push(9)
        self.assertEqual(str(sp), "3<-3<-3===3<-5<-6===9")
        


if __name__ == '__main__':
    unittest.main()




