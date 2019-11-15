
# https://runestone.academy/runestone/books/published/pythonds/Trees/BinaryHeapImplementation.html
class BinHeap:
    def __init__(self):
        self.heaplist = [0] # we keep a 0 element in the list for simpler integer division
        self.size = 0


    def get_parent(self, i):
    	return self.heapList[i // 2]

    def get_child(self, i):
    	return self.heapList[i*2+1]

    def percUp(self,i):
    	moving_up = True
    	while i // 2 > 0: #while there is a parent 1 //2 =0 so then it breaks
      		if self.heapList[i] < self.get_parent(i):
         		tmp = self.get_parent(i)
         		self.heapList[i // 2] = self.heapList[i]
         		self.heapList[i] = tmp
         		moving_up = True
         	if moving_up == False:
         		break
      		i = i // 2
      	 	moving_up = False

    def insert(self,k):
    	self.heapList.append(k) # FIX THIS SO IT DOUBLEEEEEES SEE VIDEO FROM GAYLE
    	self.currentSize = self.currentSize + 1
    	self.percUp(self.currentSize)


    def percDown(self,i):
    	moving_down = True
    	while (i * 2) <= self.currentSize: # while i has at least child
        	minchild_index = self.minChild(i)
        	if self.heapList[i] > self.heapList[minchild_index]:
            	tmp = self.heapList[i]
            	self.heapList[i] = self.heapList[minchild_index]
            	self.heapList[minchild_index] = tmp
            	moving_down = True
        	if moving_down == False:
         		break
        	moving_down = False
        	i = minchild_index


    def minChild(self,i):
    	if i * 2 + 1 > self.currentSize: #we assume that i has a child when we call this function 
        	return i * 2
    	else:
        	if self.heapList[i*2] < self.heapList[i*2+1]:
            	return i * 2
        	else:
            	return i * 2 + 1


    def delMin(self):
    	retval = self.heapList[1]
    	self.heapList[1] = self.heapList[self.currentSize]
    	self.heapList.pop() # because we put the last item to the top we have to remove the last item
    	self.currentSize = self.currentSize - 1
    	self.percDown(1)
    	return retval





