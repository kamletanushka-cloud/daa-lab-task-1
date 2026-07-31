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

---

# Repository Files

- README.md
- part1_trace.py
- part2_stack_queue.py
- part3_tree.py

---

# Time Complexity

- Part 1 (Finding Maximum): **O(n)**
- Part 1 (Sorting): **O(n log n)**
- Part 2 (Stack/Queue): **O(n)**
- Part 3 (Level Order Traversal): **O(n)**

---

# Conclusion

This assignment demonstrates the basic concepts of Design and Analysis of Algorithms, including searching, sorting, stack, queue, tree traversal, and time complexity analysis using Python.