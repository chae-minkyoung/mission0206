import random

class Node:
    def __init__(self):
        self.data=None
        self.link=None

def print_nodes(start):
    current=start
    if current == None:
        return
    print(current.data,end=' ')
    while current.link != head:
        current = current.link
        print(current.data, end=' ')
    print()
def make_list(convenience):
    global head, current, pre

    node=Node()
    node.data=convenience
    current=node

    if head==None:
        head=node
        head.link=head
        return

    if convenience[1] < head.data[1]:
        node.link = head
        last = head
        while last.link != head:
            last = last.link
        last.link =node
        head = node
        return
    current=head
    while current.link != head:
        pre = current
        current = current.link
        if convenience[1] < current.data[1]:
            pre.link = node
            node.link = current
            return

    current.link=node
    node.link = head




if __name__=='__main__':
    head, current, pre = None,None,None
    a = ['A', 'B', 'C', 'D', 'E']
    conveniences = []
    for i in range(len(a)):
        x = random.randint(1, 100)
        y = random.randint(1, 100)
        b = (x ** 2 + y ** 2) ** (1 / 2)
        c = (a[i], b)
        conveniences.append(c)
    print(conveniences)
    for convenience in conveniences:
        make_list(convenience)
    print_nodes(head)