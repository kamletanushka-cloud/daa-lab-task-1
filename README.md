# DAA Lab Task 1

## Student Details

Name: Tanushka Kamle

---

# Part 1 - Trace It Yourself

## Input

8, 3, 15, 6, 2

## Output

Largest Number: 15

Sorted List: 2, 3, 6, 8, 15

Comparisons Made: 4

## Dry Run

i = 1, A[i] = 3, max = 8, comparisons = 1

i = 2, A[i] = 15, max = 15, comparisons = 2

i = 3, A[i] = 6, max = 15, comparisons = 3

i = 4, A[i] = 2, max = 15, comparisons = 4

## Sorting Method Used

Python built-in `sorted()` function

## Explanation

The program checks each element one by one to find the largest number. Since every element must be checked once, the total number of comparisons is 4. The list is then sorted in ascending order.

---

# Part 2 - Stack or Queue

## Stack Order (LIFO)

Task5

Task4

Task3

Task2

Task1

## Queue Order (FIFO)

Task1

Task2

Task3

Task4

Task5

## Printer Should Use

Queue (FIFO)

## Reason

A printer prints jobs in the same order they arrive. Queue follows the First In First Out (FIFO) principle, making it suitable for printer scheduling.

---

# Part 3 - Build a Small Tree

## Tree Structure

```
        Root
       /    \
    Math   Science
    /  \     /   \
Algebra Geometry Physics Chemistry
```

## Level Order Traversal

Math

Science

Algebra

Geometry

Physics

Chemistry

## Explanation

Level order traversal visits all nodes level by level from left to right. It starts with the top-level nodes and then moves to the next level until every node has been visited.


## Part 4. Count the Steps

### Input:
- Single loop: 1 to 5
- Single loop: n = 20
- Nested loop: i = 1 to 5, j = 1 to 5
- Nested loop: n = 10

### Output:
- Single loop runs: 5 times
- Single loop for n = 20: 20 times
- Nested loop runs: 25 times
- Nested loop for n = 10: 100 times

### Dry Run:

1. Single loop (1 to 5):
   - The loop executes 5 times.
   - Each iteration prints the value of i.

2. Single loop (n = 20):
   - The loop executes 20 times.

3. Nested loop (1 to 5):
   - The outer loop executes 5 times.
   - The inner loop executes 5 times for each outer iteration.
   - Total executions = 5 × 5 = 25.

4. Nested loop (n = 10):
   - Total executions = 10 × 10 = 100.

### Explanation:

A single loop has linear time complexity O(n) because the number of operations increases proportionally with the input size.

A nested loop has quadratic time complexity O(n²) because the inner loop executes n times for every iteration of the outer loop. Therefore, the number of operations increases more rapidly as the input size grows.

---


## Repository Files

- README.md
- part1_trace.py
- part2_stack_queue.py
- part3_tree.py
- part4_complexity.py


---


## Time Complexity

- Part 1 (Finding Maximum): O(n)
- Part 1 (Sorting): O(n log n)
- Part 2 (Stack/Queue): O(n)
- Part 3 (Level Order Traversal): O(n)
- Part 4 (Single Loop): O(n)
- Part 4 (Nested Loop): O(n²)


---

# Conclusion

This assignment demonstrates the basic concepts of Design and Analysis of Algorithms, including searching, sorting, stack, queue, tree traversal, and time complexity analysis using Python.