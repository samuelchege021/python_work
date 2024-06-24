#create node
#create  linked list
#add mode to the linked list
#print linklist

class Node:
   def __init__(self,data):
       self.data=data
       self.next=None

class linkedlist:
    def __init__(self):
        self.head=None



    def insert(self,newNode):
        #head=>john=>none
        if self.head==None:
            self.head=newNode

        else:
            #head john>ben>none
            #self.head.next=newNode
            lastNode=self.head
            while True:
                if lastNode.next is None:
                    break

                lastNode=lastNode.next
            lastNode=newNode


    def printlist(self):
      if self.head is None:
          print("list is empty")
      currentNode=self.head
      while True:
           if currentNode is None:
            break
           print(currentNode.data)
           currentNode=currentNode.next

#Node =>data,next



#firstnode.data=>john  firstnode.next=>None
fisrtNode=Node("john")
linkedlist=linkedlist()
linkedlist.insert(fisrtNode)
secondNode=Node("ben")
linkedlist.insert(secondNode)
thirdNode=Node("mathew")
linkedlist.insert(thirdNode)
linkedlist.printlist()