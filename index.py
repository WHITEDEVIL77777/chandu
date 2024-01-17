

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def insertatend(self,data):
        newnode=Node(data)
        if self.head==None:
            self.head=self.tail=newnode
        else:
            self.tail.next=newnode
            self.tail=newnode

            
    def insertatbegining(self,data):
        newnode=Node(data)
        if self.head==None:
            self.head=self.tail=newnode
        else:
            newnode.next=self.head
            self.head=newnode

            
    def insertat(self, data, position):
        newnode = Node(data)
        if position == 0:
            newnode.next = self.head
            self.head = newnode
            return
        current = self.head
        for i in range(position - 1):
            if current is None:
                raise IndexError("Position out of bounds")
            current = current.next
        newnode.next = current.next
        current.next = newnode

    def deleteatend(self):
        if self.head==None:
            print("list is empty\n")
        else:
            current=self.head
            prev=None
            while current!=self.tail:
                prev=current
                current=current.next
            if current==self.head:
                self.head=self.tail=None
            else:
                self.tail=current
                current.next=None

    def deleteatbegining(self):

        current=self.head
        if self.head==None:
            print("list is empty")
        
        else:
           
            current=self.head.next
            self.head=current



    def delete(self,pos):
        if pos==0:
            self.head=self.head.next
        else:
            current=self.head
            for i in range(pos-1):
               current=current.next
        current.next=current.next.next
            
        
        

    def print_list(self):
        if self.head==None:
            print("the linked list  is empty\n") 
        
        current=self.head
        while current!=None:
            print(current.data,"->",end=" ")
            current=current.next


linked_list = LinkedList()


while True:
        print("select operation")
        print("1.INSERTT AT END")
        print("2.INSERTT AT BEGINING")
        print("3.INSERTT AT PARTICULAR POSITIN")
        print("4.DELETE AT END")
        print("5.DELETE AT BEGINING")
        print("6.DELETE AT PARTICULAR POSITION")
        print("7.DISPLAY THE LINKED LIST")
        print("\n")
        choice=input("Enter Your Choice  :\n")
   
        if choice=='1':
            node=input("Enter The Data You Want To Insert:  \n ")
            print("INSERT AT END\n",linked_list.insertatend(node))
            
            linked_list.print_list()
            print("\n")
        elif choice=='2':
            node=input("Enter The Data You Want To Insert:  \n ")
            print("INSERT AT BEGINING\n",linked_list.insertatbegining(node))
            
            linked_list.print_list()
            print("\n")


        elif choice=='3':
            node=input("Enter The Data You Want To Insert:  \n ")
            Y=int(input("enter number u want to insert in partiular position\n"))
            print("INSERT AT PARTICULAR POSITION\n",linked_list.insertat(node,Y))
            
            linked_list.print_list()
            print("\n")


        elif choice=='4':
            print("DELETE AT END\n",linked_list.deleteatend())
            
            linked_list.print_list()
            print("\n")

        elif choice=='5':
            print("DELETE AT BEGINING\n",linked_list.deleteatbegining())
            
            linked_list.print_list()
            print("\n")
        elif choice=='6':
            S=int(input("enter number u want to insert in partiular position\n"))
            print("DELETE AT PARTICULAR POSITION\n",linked_list.delete(S))
            
            linked_list.print_list()
            print("\n")
        elif choice=='7':
            print("DISPLAYING THE LINKED LIST\n")
            linked_list.print_list()
            print("\n")

        next=input("u like to do next operation?(1/0):\n")
        if next=="0":
            break
else:
            print("invalid input")


        

