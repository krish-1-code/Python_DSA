class single_node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next   

    def __str__(self):
        return str(self.data)

class double_node:
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.data)

Head = single_node(1)
A = single_node(10)
B = single_node(20)

Head.next = A
A.next = B

#Traversing the linked list

rn = Head
elements = []
while rn:
    elements.append(str(rn.data))
    rn = rn.next
print('->'.join(elements))

#Searching In linekd list: O[n]

search = Head 
look = input("Enter a value: ")
while search:
    if str(search) == look:
        print(f"{look} is in the linked list")
        break
    search = search.next
