Python library providing useless calculations for geometrical shapes, such as finding an area or perimeter.

# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = ah

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

# Code reference

## circle.py

### area(r)
Find area of the circle

**Arguments**
- `r: float` - Radius of the circle 

**Returns**
- `out: float` - Area of the circle

**Example**
```python
import circle

radius = 3
print(circle.area(radius)) # -> 28.274333882308138
```

### perimeter(r)
Find perimeter of the circle

**Arguments**
- `r: float` - Radius of the circle 

**Returns**
- `out: float` - Perimeter of the circle

**Example**
```python
import circle

radius = 3
print(circle.perimeter(radius)) # -> 18.84955592153876
```

## rectangle.py

### area(a, b)
Find area of the rectangle

**Arguments**
- `a: float` - One side of the rectangle
- `b: float` - Another side of the rectangle

**Returns**
- `out: float` - Area of the rectangle

**Example**
```python
import rectangle

print(rectangle.area(3, 7)) # -> 21
```

### perimeter(a, b)
Find perimeter of the rectangle

**Arguments**
- `a: float` - One side of the rectangle
- `b: float` - Another side of the rectangle

**Returns**
- `out: float` - Perimeter of the rectangle

**Example**
```python
import rectangle

print(rectangle.perimeter(3, 7)) # -> 20
```

## square.py

### area(a)
Find area of the square

**Arguments**
- `a: float` - Side of the square

**Returns**
- `out: float` - Area of the square

**Example**
```python
import square

side = 5
print(square.area(side)) # -> 25
```

### perimeter(a)
Find perimeter of the square

**Arguments**
- `a: float` - Side of the square

**Returns**
- `out: float` - Perimeter of the square

**Example**
```python
import square

side = 5
print(square.perimeter(side)) # -> 20
```

## triangle.py

### area(a, h)
Find area of the triangle

**Arguments**
- `a: float` - Any side of the triangle
- `h: float` - Height of the triangle, corresponding to the given side

**Returns**
- `out: float` - Area of the triangle

**Example**
```python
import triangle

side = 6
height = 4
print(triangle.area(side, height)) # -> 12.0
```

### perimeter(a, b, c)
Find perimeter of the triangle

**Arguments**
- `a: float` - One side of the trigangle
- `b: float` - Second side of the trigangle
- `c: float` - Third side of the trigangle

**Returns**
- `out: float` - Perimeter of the triangle

**Example**
```python
import triangle

print(triangle.perimeter(2, 3, 4)) # -> 9
```

# Commit history
## 2.10.2024
### 0634252
- Functions been made strict typed
- Added in-code docs
### c1ae219
- New module triangle.py
### c100412
- New module rectangle.py
## 4.03.2021
### d078c8d
- Created readme.md
### 8ba9aeb
- New module circle.py
- New module square.py