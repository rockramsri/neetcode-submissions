class PrefixNode:
    def __init__(self):
        self.listOfnodes={}
        self.isItEnd=False
class PrefixTree:
    def __init__(self):
        self.node=PrefixNode()
    def insert(self, word: str) -> None:
        head=self.node
        i=0
        while i<len(word) and word[i] in head.listOfnodes:
            head=head.listOfnodes[word[i]]
            i+=1
        while i<len(word):
            head.listOfnodes[word[i]]=PrefixNode()
            head=head.listOfnodes[word[i]]
            i+=1
        head.isItEnd=True
        #print(self.listOfnodes)
    def search(self, word: str) -> bool:
        head=self.node
        for i in word:
            if i in head.listOfnodes:
                head=head.listOfnodes[i]
            else:
                return False
        return head.isItEnd
    def startsWith(self, prefix: str) -> bool:
        head=self.node
        for i in prefix:
            if i in head.listOfnodes:
                head=head.listOfnodes[i]
            else:
                return False
        return True

            
        
        