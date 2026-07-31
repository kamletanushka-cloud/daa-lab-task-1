from collections import deque

tasks = ["Task1", "Task2", "Task3", "Task4", "Task5"]

print("Stack (LIFO)")
stack = []

for task in tasks:
    stack.append(task)

while stack:
    print(stack.pop())

print()

print("Queue (FIFO)")
queue = deque(tasks)

while queue:
    print(queue.popleft())

print()
print("Printer should use Queue because it prints jobs in the order they arrive.")