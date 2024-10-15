# # command=""
# # started=False
# # while True:
# #     command=input(">> ").lower()
# #     if command=="start":
        
# #         if started:
# #             print("car already started")
# #         else:
# #             started=True
# #             print("car started")
            
# #     elif command=="stop":
# #         if  not started:
# #             print("car already stopped")
# #         else:
# #             started = False
# #             print("car stopped")
            
# #     elif command=="quit":
# #         break
# #     else:
# #         print("enter the appropriate command")


# #Selection sort
# def selection_sort(n,list):
#     # n=int(input())
#     # list= []
#     # for i in range(n):
#     #     element=int(input())
#     #     list.append(element)
#     for i in range(n):
        
#         min=i
        
#         for j in range(i+1,n):
            
#             if list[j] < list[min]:
#                 min = j
#         (list[i],list[min])=(list[min],list[i])
  
# list=[2,61,6,82,32]
# n=len(list)
# selection_sort(n,list)
# print(list)

# #Bubble sort
# def Bubble_sort(n,arr):
#     for i in range(n):
#         swapped = False
#         for j in range(0,n-i-1):
#             if arr[j]>arr[j+1]:
#                 (arr[j],arr[j+1])=(arr[j+1],arr[j])
#                 swapped = True
#         if swapped:
#             break
# arr=[1,2,3,4,5]
# n=len(arr)
# Bubble_sort(n,arr)
# print(arr)

# #Insertion sort
# def insertion_sort(n,arr):
#     if n <= 1:
#         return
#     for i in range(1,n):
#         key = arr[i]
#         j = i-1
#         while j>=0 and key<arr[j]:
#             arr[j+1]=arr[j]
#             j=j-1        
#         arr[j+1]=key
# arr=[11,2,13,34,5]
# n=len(arr)
# insertion_sort(n,arr)
# print(arr)

# #Mergesort

# def merge_sort(arr):
#     #base case
#     if len(arr)<=1:
#         return arr
#     mid=len(arr)//2
#     left=merge_sort(arr[:mid])
#     right=merge_sort(arr[mid:])
#     return merge(left,right)
# def merge(left,right):
#     sorted_arr=[]
#     i=j=0
#     while i<len(left) and j<len(right):
#         if left[i]<right[j]:
#             sorted_arr.append(left[i])
#             i+=1
#         else:
#             sorted_arr.append(right[j])
#             j+=1
#     while i<len(left):
#         sorted_arr.append(left[i])
#         i+=1
#     while j<len(right):
#         sorted_arr.append(right[j])
#         j+=1
#     return sorted_arr
# arr = [3, 7, 6, -10, 15, 23.5, 55, -13]
# sorted_arr = merge_sort(arr)
# print("Sorted array:", sorted_arr)

# #Quicksort
# def quick_sort(arr,low,high):
#     if low<high:
#         pi=partition(arr,low,high)
#         quick_sort(arr,low,pi-1)
#         quick_sort(arr,pi+1,high)
# def partition(arr,low,high):
#     pivot=arr[low]
#     i=low+1
#     for j in range(low+1,high+1):
#         if arr[j]<pivot:
#             arr[i],arr[j]=arr[j],arr[i]
#             i+=1
#     arr[low], arr[i - 1] = arr[i - 1], arr[low]

#     return i - 1 
# arr = [38, 27, 43, 3, 9, 82, 10]
# quick_sort(arr, 0, len(arr) - 1)
# print("Sorted array:", arr)


#LINKED LISTS

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def traversAndPrint(head):
    currentNode=head
    while currentNode:
        print(currentNode.data,end="->")
        currentNode=currentNode.next
    print("null")

def findLowest(head):
    minValue=head.data
    currentNode=head.next
    while currentNode:
        if currentNode.data<minValue:
            minValue=currentNode.data
        currentNode=currentNode.next
    return minValue

def deleteNode(head,nodeToDel):
    if head==nodeToDel:
        return head
    currentNode=head
    while currentNode.next and currentNode.next!=nodeToDel:
        currentNode=currentNode.next
    if currentNode.next is None:
        return head
    currentNode.next=currentNode.next.next
    return head
def insertNode(head,newNode,pos):
    if pos==1:
        newNode.next=head
        return newNode
    currentNode=head
    for i in range(pos-2):
        if currentNode is None:
            break
        currentNode=currentNode.next
    newNode.next=currentNode.next
    currentNode.next=newNode
    return head

node1=Node(2)
node2=Node(9)
node3=Node(1)
node4=Node(15)
node5=Node(10)

#connecting node
node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5

traversAndPrint(node1)
print(findLowest(node1))

print("Before deletion:")
traversAndPrint(node1)

# Delete node4
node1 = deleteNode(node1, node4)

print("\nAfter deletion:")
traversAndPrint(node1)

print("Original list:")
traversAndPrint(node1)

# Insert a new node with value 97 at position 2
newNode = Node(97)
node1 = insertNode(node1, newNode, 2)

print("\nAfter insertion:")
traversAndPrint(node1)

#Doubly linkedlist
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
node1 = Node(3)
node2 = Node(5)
node3 = Node(13)
node4 = Node(2)

node1.next = node2

node2.prev = node1
node2.next = node3

node3.prev = node2
node3.next = node4

node4.prev = node3

print("\nTraversing forward:")
currentNode = node1
while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
print("null")

print("\nTraversing backward:")
currentNode = node4
while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.prev
print("null")

#circular linkedlist
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
node1 = Node(3)
node2 = Node(5)
node3 = Node(13)
node4 = Node(2)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node1

currentNode = node1
startNode = node1
print(currentNode.data, end=" -> ") 
currentNode = currentNode.next 

while currentNode != startNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next

print("...")

#circular doubly linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

node1 = Node(3)
node2 = Node(5)
node3 = Node(13)
node4 = Node(2)

node1.next = node2
node1.prev = node4

node2.prev = node1
node2.next = node3

node3.prev = node2
node3.next = node4

node4.prev = node3
node4.next = node1

print("\nTraversing forward:")
currentNode = node1
startNode = node1
print(currentNode.data, end=" -> ")
currentNode = currentNode.next

while currentNode != startNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
print("...")

print("\nTraversing backward:")
currentNode = node4
startNode = node4
print(currentNode.data, end=" -> ")
currentNode = currentNode.prev

while currentNode != startNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.prev
print("...")


#Stack
class Stack:
    def __init__(self):
        self.stack=[]

    def push(self,element):
        self.stack.append(element)
    
    def pop(self):
        if self.isEmpty():
            return "stack is empty"
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return "stack is empty"
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack)==0
    
    def size(self):
        return len(self.stack)
    
myStack= Stack()
myStack.push('A')
myStack.push('B')
myStack.push('C')
print("Stack: ", myStack.stack)

print("Pop: ", myStack.pop())

print("Peek: ", myStack.peek())

print("isEmpty: ", myStack.isEmpty())

print("Size: ", myStack.size())

#Stack with LL
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def push(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        popped_node = self.head
        self.head = self.head.next
        self.size -= 1
        return popped_node.value
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.head.value
    
    def isEmpty(self):
        return self.size == 0
    
    def stackSize(self):
        return self.size

myStack = Stack()
myStack.push('A')
myStack.push('B')
myStack.push('C')

print("Pop: ", myStack.pop())
print("Peek: ", myStack.peek())
print("isEmpty: ", myStack.isEmpty())
print("Size: ", myStack.stackSize())

#Queue
class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, element):
        self.queue.append(element)
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue[0]
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)

# Create a queue
myQueue = Queue()

myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')
print("Queue: ", myQueue.queue)

print("Dequeue: ", myQueue.dequeue())

print("Peek: ", myQueue.peek())

print("isEmpty: ", myQueue.isEmpty())

print("Size: ", myQueue.size())

#Queue with LL
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0
    
    def enqueue(self, element):
        new_node = Node(element)
        if self.rear is None:
            self.front = self.rear = new_node
            self.length += 1
            return
        self.rear.next = new_node
        self.rear = new_node
        self.length += 1
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        temp = self.front
        self.front = temp.next
        self.length -= 1
        if self.front is None:
            self.rear = None
        return temp.data
    
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.front.data
    
    def isEmpty(self):
        return self.length == 0
    
    def size(self):
        return self.length

    def printQueue(self):
        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

# Create a queue
myQueue = Queue()

myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')
print("Queue: ", end="")
myQueue.printQueue()

print("Dequeue: ", myQueue.dequeue())

print("Peek: ", myQueue.peek())

print("isEmpty: ", myQueue.isEmpty())

print("Size: ", myQueue.size())