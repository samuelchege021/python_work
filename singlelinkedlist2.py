class Node:
    def __init__(self,data):

      self.data=data
      self.next=next


class linkedlist():

    def __int__(self):
        self.head=None


    def insert(self,newNode):

        if self.head==None:
            self.head=newNode

        else:
            lastnode=self.head
             while True:
               if lastnode.next is None:
                   lastnode.next=lastnode
                lastnode=newnode

     def printlist(self)
         if self.head==None:
             currentnode=self.head
         while True:
             print(currentnode.data)
              currentnode=currentnode.next



linkedlist=linkedlist()
firstnode=Node("john")
linkedlist.insert(firstnode)
