"""Calculations for triangle"""

def area(a: float, h: float) -> float:
    """Find area of the triangle
    
    Args:
        a: Any side of the triangle
        h: Height of the triangle, corresponding to the given side

    Returns:
        Area of the triangle
    """
    return a * h / 2 

def perimeter(a: float, b: float, c: float) -> float:
    """Find perimeter of the triangle
    
    Args:
        a: One side of the trigangle
        b: Second side of the trigangle
        c: Third side of the trigangle

    Returns:
        Perimeter of the triangle
    """ 
    return a + b + c