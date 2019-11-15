

class TrieNode():

    def __init__(self, myval):
        self.iscompleteword = False
        #mapping from letter to child node
        self.children = {} 

class Trie():

    def __init__(self):
        self.root = TrieNode("*")

    
    def insert(self, myword):
        currentnode = self.root
        while len(myword)>0:
            letter = myword[0]
            myword = myword[1:]
            if letter not in currentnode.children:
                newnode = TrieNode(letter)
                currentnode.children[letter] = newnode
                if len(myword)==0:
                    newnode.iscompleteword = True
            currentnode = newnode
        return myword


    def search(self, myword):
        currentnode = self.root
        while len(myword)>0:
            letter = myword[0]
            try:
                currentnode = currentnode.children[letter]
            except:
                return False
            myword = myword[1:]
        if currentnode.iscompleteword ==True:
            return True
        else:
            return False


    def startsWith(self, myword):
        currentnode = self.root
        while len(myword)>0:
            letter = myword[0]
            try:
                currentnode = currentnode.children[letter]
            except:
                return False
            myword = myword[1:]
        return True


myTrie = Trie()

myTrie.insert("abdde")

print(myTrie.search("abd"))
print("------")
print(myTrie.startsWith("abd"))
print("------")
print(myTrie.search("abdde"))







