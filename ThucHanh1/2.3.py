# Queue implementation using list

# Initializing a queue
queue = []

# push elements to the end of the list
print("append")
queue.append(5)
queue.append(3)
queue.append(7)
queue.append(4)
queue.append(2)

# print the queue
print(queue)

print("--------------------------------------")
# get elements from the beginning
print("pop")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

# print the queue
print(queue)
print("--------------------------------------")
# Class Queue to represent a queue

print("class Queue")
class Queue:
    # __init__ function
    def __init__(self, capacity):
        self.front = self.size = 0
        self.rear = capacity -1
        self.Q = [None]*capacity
        self.capacity = capacity

    # Queue is full when size becomes
    # equal to the capacity
    def isFull(self):
        return self.size == self.capacity

    # Queue is empty when size is 0
    def isEmpty(self):
        return self.size == 0

    # Function to add an item to the queue.
    # It changes rear and size
    def enQueue(self, item):
        if self.isFull():
            print("Full")
            return
        self.rear = (self.rear + 1) % (self.capacity)
        self.Q[self.rear] = item
        self.size = self.size + 1
        print("% s enqueued to queue"  % str(item))

    # Function to remove an item from queue.
    # It changes front and size
    def deQueue(self):
        if self.isEmpty():
            print("Empty")
            return

        print("% s dequeued from queue" % str(self.Q[self.front]))
        self.front = (self.front + 1) % (self.capacity)
        self.size = self.size -1

    # Function to get front of queue
    def que_front(self):
        if self.isEmpty():
            print("Queue is empty")

        print("Front item is", self.Q[self.front])

    # Function to get rear of queue
    def que_rear(self):
        if self.isEmpty():
            print("Queue is empty")
        print("Rear item is",  self.Q[self.rear])


# Driver Code
if __name__ == '__main__':
    queue = Queue(30)
    queue.enQueue(10)
    queue.enQueue(20)
    queue.enQueue(30)
    queue.enQueue(40)
    queue.deQueue()
    queue.que_front()
    queue.que_rear()