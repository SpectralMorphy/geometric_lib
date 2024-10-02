"Calculations for rectangle"

def area(a: float, b: float) -> float:
    """Find area of the rectangle
    
    Args:
        a: One side of the rectangle
        b: Another side of the rectangle

    Returns:
        Area of the rectangle
    """
    return a * b 

def perimeter(a: float, b: float) -> float: 
    """Find perimeter of the rectangle
    
    Args:
        a: One side of the rectangle
        b: Another side of the rectangle

    Returns:
        Perimeter of the rectangle
    """
    return 2 * (a + b)