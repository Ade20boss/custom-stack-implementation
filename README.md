# Fixed-Capacity Python Stack

A robust, educational implementation of a Stack data structure in Python. This class enforces a fixed capacity to simulate memory constraints and utilizes strict LIFO (Last-In, First-Out) logic for all operations, including searching.



## Features

* **Fixed Capacity:** The stack is initialized with a hard limit of **64 items**, simulating a fixed-size buffer.
* **Overflow Protection:** Prevents pushing new items once the capacity is reached.
* **Underflow Protection:** Prevents popping or peeking when the stack is empty.
* **Verbose Logging:** Provides clear console feedback for success, warnings, and error states (e.g., `[STACK OVERFLOW ERROR]`).
* **Destructive Search:** Simulates a physical stack search where items must be removed to find elements deeper in the stack.

## Getting Started

### Prerequisites
You only need a standard Python 3 installation to run this code.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Ade20boss/custom-stack-implementation.git
   ```
2. Navigate to the directory:
  ```bash
    cd your-repo-name
  ```

### Usage

You can import the `Stack` class into your own scripts or run the file directly to see the demo.

```python
from stack import Stack

# Initialize
my_stack = Stack()

# Push items
my_stack.push("Book A")
my_stack.push("Book B")

# Peek at the top item
print(my_stack.peek()) # Output: "Book B"

# Remove items
my_stack.pop_stack()

```

## API Reference

### `push(item)`

Adds an item to the top of the stack.

* **Checks:** Verifies if `len(items) == capacity`.
* **Output:** Prints a success message or an Overflow Error if full.

### `pop_stack()`

Removes and returns the item at the top of the stack.

* **Checks:** Verifies if the stack is empty.
* **Output:** Returns the item or `None` if empty (with an Underflow Error message).

### `peek()`

Returns the item at the top of the stack *without* removing it.

* **Output:** Returns the item or `None` if empty.

### `search(item)`

**⚠️ Warning: This is a destructive operation.**
To adhere to strict Stack physics, this method searches for an item by peeking at the top. If the top item is not the target, it **pops (removes)** it and checks the next one.

* **Behavior:** It will strip the stack down until the item is found or the stack is empty.
* **Returns:** The item (if found) or an error message.

## Example Scenario

The following example demonstrates the capacity limit and the search behavior:

```python
stack = Stack()

# Fill the stack to capacity
for i in range(64):
    stack.push(i)

# Search for the number 1 (which is at the bottom)
# This will result in popping items 63 down to 2
print(stack.search(1)) 

```

## License

[MIT](https://choosealicense.com/licenses/mit/)
