# Day 08 — Python Lists

## 1. Lists

A list is a collection of ordered and mutable data.

Lists are written inside square brackets `[]`.

The values inside a list are separated by commas.

Lists are mutable, which means once a list is created, its
values can be changed.

A list can contain multiple data types.

### Example

```python
fruits = ["apple", "mango", "banana", 14, 45.10]
print(fruits)
```
## 2. Slicing Lists
List slicing is used to access a specific part of a list.
Example:
```python
a = ["Ironman", "Thor", "Captain", "Hulk"]

print(a[:])
print(a[1:3])
print(a[2])
print(a[1])
print(a[::-1])
print(a[-1:-4:-1])

#List indexing starts from 0.

a = ["Ironman", "Thor", "Captain", "Hulk"]

print(a[0])
print(a[1])
print(a[2])
print(a[3])

#Negative indexing starts from the last element.
print(a[-1])
print(a[-2])
```
## 3. List Iteration
Iteration means accessing the elements of a list one by one.
### 3.1 Iteration Using for Loop
```python
a = ["Hulk", "Thor", "Ironman", "Captain"]

for i in a:
    print(i)
```
### 3.2 Iteration Using for Loop with range()
The range() function can be used with len() to access list elements using their index.
```python
a = ["Hulk", "Thor", "Ironman", "Captain"]

for i in range(len(a)):
    print(a[i])
```
### 3.3 Iteration Using while Loop
```python
a = ["Hulk", "Thor", "Ironman", "Captain"]
i = 0
while i < len(a):
    print(a[i])
    i += 1
```
### 3.4 Short-hand for Loop
A list can also be iterated using a short-hand for loop.
```python
a = ["Hulk", "Thor", "Ironman", "Captain"]

[print(i) for i in a]
```
## 4. List Functions & Methods
### 4.1 len()
The len() function is used to find the length of a list.
```python
a = ["Thor", "Hulk", "Mohit", "Dan"]

print(len(a))
```
### 4.2 count()
The count() method is used to count the occurrence of an element in a list.
```python
a = ["Thor", "Hulk", "Mohit", "Dan", "Hulk"]

print(a.count("Hulk"))
```
### 4.3 append()
The append() method is used to add an element to the end of a list.
```python
a = ["Thor", "Hulk", "Mohit"]

a.append("Pisha")
print(a)
```
### 4.4 insert()
The insert() method is used to add an element at a specific position.
```python
a = ["Thor", "Hulk", "Mohit"]

a.insert(1, "Ironman")
print(a)
```
### 4.5 remove()
The remove() method removes a specific element from a list.
```python
a = ["Thor", "Hulk", "Mohit"]

a.remove("Hulk")
print(a)
```
### 4.6 pop()
The pop() method removes an element from a specific index.
```python
a = ["Thor", "Hulk", "Mohit"]

print(a.pop(1))
print(a)
```
### 4.7 copy()
The copy() method is used to create a copy of a list.
```python
a = ["Thor", "Hulk", "Ironman"]

b = a.copy()
print(b)
```
### 4.8 index()
The index() method returns the index of a specified element.
```python
a = ["Thor", "Hulk", "Ironman"]

print(a.index("Thor"))
```
### 4.9 extend()
The extend() method is used to add multiple elements from another list.
```python
a = ["Thor", "Hulk"]
c = ["Mohit", "Rohit"]

a.extend(c)
print(a)
```
### 4.10 reverse()
The reverse() method reverses the order of elements in a list.
```python
a = ["Thor", "Hulk", "Ironman"]

a.reverse()
print(a)
```
### 4.11 sort()
The sort() method sorts the elements of a list.
```python
a = [5, 2, 8, 1, 3]

a.sort()
print(a)
```
### 4.12 clear()
The clear() method removes all elements from a list.
```python
a = ["Thor", "Hulk", "Ironman"]

a.clear()
print(a)
```
