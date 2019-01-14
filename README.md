# Hanoi Towers

1. Details

2. How to use the Hanoi Tower algorithm implementation

3. License

4. Credits

## 1. Details

- The Tower of Hanoi is a logic game in which you need to transfer disks from one rod to another with special [rules](https://en.wikipedia.org/wiki/Tower_of_Hanoi)

- This algorithm is easy to implement as a recursive function, but this would be highly space-inefficient

- I came up with an algorithm which solves the Towers of Hanoi without any recursive functions, which effects in much better space- and time-efficiency

## 2. How to use the Hanoi Tower algorithm implementation

### 2.1 Installation

Clone or download this repository, then open the folder. No additional dependencies are needed.

## 2.2 Usage

First, you need to import hanoi:

```python
import hanoi
```

If you just want to output the steps needed to solve the Towers of Hanoi with n disks, type this: (Example: n=6)

```javascript
n = 6

hanoi.output(n)
```

If you want to get the disk's order and movement as a list, you have to enter this code snippet:

```python
n = 6

order = generate_order(n)
movement = generate_movement(n)

# In this example, the disk order[i] must be moved to the rod movement[i]
```

# 3. License

The algorithm and the implementation are published under the MIT License.

# 4. Credits

The algorithm and the implementation are developed by Tim-Luca Lagmöller.


