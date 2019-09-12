# 3.1 
class ThreeStacks:
    def __init__(self, cap):
        self.capacity = cap
        self.lst = [None] * 3 * cap
        self.size = [0,0,0]
 
    def push(self, data, stackNum):
        if stackNum < 3 and stackNum >= 0:
            if self.isFull(stackNum):
                print("Full - please pop")
                return False
            self.size[stackNum] = self.size[stackNum]+1
            topindex = self.indexOfTop(stackNum)
            self.lst[topindex] = data
        return True

 
    def pop(self, stackNum):
        if stackNum < 3 and stackNum >= 0:
            if self.isEmpty(stackNum):
                print("Empty")
                return False
            topindex = self.indexOfTop(stackNum)
            temp = self.lst[topindex]
            self.lst[topindex] = None
            self.size[stackNum] = self.size[stackNum]-1
            return temp
 
    def size(self, stackNum):
         return self.top[stackNum]

    def isFull(self, stackNum):
        if self.size[stackNum] >= self.capacity:
            return True

    def isEmpty(self, stackNum):
        if self.size[stackNum] <= 0 :
            return True

    def indexOfTop(self, stackNum):
        offset = stackNum*self.capacity
        index = self.size[stackNum]+offset
        return index

import unittest

class TestStringMethods(unittest.TestCase):

    def test_array_stack(self):

        my3 = ThreeStacks(3)
        self.assertEqual(my3.push(-100,0), True)
        self.assertEqual(my3.push(-110,0), True)
        self.assertEqual(my3.push(-10,0), True)
        self.assertEqual(my3.push(-20,0), False)
        self.assertEqual(my3.pop(0), -10)
        self.assertEqual(my3.pop(0), -110)
        self.assertEqual(my3.pop(0), -100)
        self.assertEqual(my3.pop(0), False)
        self.assertEqual(my3.push(-200,1), True)
        self.assertEqual(my3.push(-210,1), True)
        self.assertEqual(my3.pop(1), -210)
        self.assertEqual(my3.pop(1), -200)

        self.assertEqual(my3.push(-300,2), True)
        self.assertEqual(my3.push(-310,2), True)
        self.assertEqual(my3.pop(2), -310)
        self.assertEqual(my3.push(-210,1), True)
        self.assertEqual(my3.pop(2), -300)        


if __name__ == '__main__':
    unittest.main()
