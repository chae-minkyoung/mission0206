class Node():
    def __init__(self):
        self.data=None
        self.link=None
        self.reverse=None
def print_node(start):
    current = start
    print("정방향 -->",end = ' ')
    if current.link == None:
        return
    while current.link!=None:
        print(current.data, end= ' ')
        current=current.link
    print(current.data)
def print_rnode(start):
    current = start
    print("역방향 -->",end = ' ')
    if current.reverse == None:
        return
    while current.reverse!=None:
        print(current.data, end= ' ')
        current=current.reverse
    print(current.data)
if __name__=="__main__":
    Array=['다현','정연','쯔위','사나','지효']
    node=Node()
    node.data=Array[0]
    head=node
    current = node
    for member in Array[1:]:
        pre = node
        node=Node()
        current=node
        pre.link=node
        node.data=member
    print_node(head)

    node = Node()
    node.data= Array[-1]
    head=node
    current=node
    for member in Array[-2::-1]:
        pre=node
        node=Node()
        current=node
        pre.reverse=node
        node.data=member
    print_rnode(head)