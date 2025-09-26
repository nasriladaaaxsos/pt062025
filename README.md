# Exercise: Implement basic operations for Stacks and Queues using python

## 📌 Overview  
This project is a simple exercise to practice **data structures** in Python.  
It provides a skeleton implementation for **Stack** and **Queue** classes, along with a **Node** class for linked list representation.  

The goal is to complete the missing methods and implement basic operations such as push, pop, enqueue, dequeue, and print.  

---

## 🗂 Project Structure  

- `Stack.py` — Stack class (push, pop, is_empty, etc.)
- `Queue.py` — Queue class (enqueue, dequeue, is_empty, etc.)
- `Node.py` — Node class for linked list structure
- `main.py` — Create instances and test the data structures
- `README.md` — Project documentation




---

## 🧩 Classes & Methods  

### 🔹 Node  
Represents a single element in the stack/queue.  
- `data`: stores the value  
- `next`: pointer to the next node  

### 🔹 Stack  
Implements **LIFO (Last In, First Out)** structure.  
- `push_element(value)` → Insert element at the top  
- `pop_element()` → Remove and return top element  
- `is_empty()` → Check if stack is empty  
- `get_top()` → Peek top element  
- `print_stack()` → Print stack elements  

### 🔹 Queue  
Implements **FIFO (First In, First Out)** structure.  
- `enqueue(value)` → Insert element at the rear  
- `dequeue()` → Remove and return front element  
- `is_empty()` → Check if queue is empty  
- `get_peek()` → Peek front element  
- `print_queue()` → Print queue elements  

---

## 🚀 Getting Started  

1. **Clone the repository**  
   ```bash
   git clone [https://github.com/your-username/stacks-queues-exercise.git](https://github.com/nasriladaaaxsos/pt062025.git)
   cd stacks-queues-exercise

2. **Run the program**
Implement the missing methods in Stack.py and Queue.py, then test in Driver.py.



## 🎯 Learning Objectives  

By completing this exercise, you will be able to:  

- Understand the concept of **Stacks (LIFO – Last In, First Out)**  
- Understand the concept of **Queues (FIFO – First In, First Out)**  
- Implement basic operations for stacks and queues using **linked list nodes**  
- Practice **object-oriented programming (OOP)** principles in Python  
- Gain hands-on experience with **manual data structure implementation** without using built-in lists  



## 📝 Example Usage  

After implementing the missing methods in `Stack.py` and `Queue.py`, you can test the classes like this:

```python
from Stack import Stack
from Queue import Queue

# --- Stack Example ---
stack = Stack()
stack.push_element(10)
stack.push_element(20)
stack.print_stack()          # Expected Output: 20 -> 10
print("Popped:", stack.pop_element())  # Expected Output: Popped: 20
print("Top element:", stack.get_top()) # Expected Output: Top element: 10

# --- Queue Example ---
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.print_queue()          # Expected Output: 1 -> 2
print("Dequeued:", queue.dequeue())   # Expected Output: Dequeued: 1
print("Front element:", queue.get_peek()) # Expected Output: Front element: 2

