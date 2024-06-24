class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def insertAtbegin(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return

        else:
            new_node.next=self.head
            self.head=new_node

    def insertAtindex(self,data,index):
        new_node=Node(data)
        current_node=self.head
        position=0

        if position==index:
            self.insertAtbegin(data)

        else:
            while(current_node !=None and position+1 !=index):
                position=position+1
                current_node=current_node.next

            if current_node !=None:
                new_node.next=current_node.next
                current_node.next=new_node

            else:
             print("index not found")





    def print_list(self):
            current_node=self.head
            while current_node is not None:
                print(current_node.data,end="->")
                current_node=current_node.next
            print("None")




ll=LinkedList()
ll.insertAtbegin('c')
ll.insertAtindex("b",1)

ll.print_list()
