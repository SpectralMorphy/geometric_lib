"""Calculations for circle"""

import math

def area(r: float) -> float:
    """Find area of the circle
    
    Args:
        r: Radius of the circle

    Returns:
        Area of the circle
    """
    return math.pi * r * r


def perimeter(r: float) -> float:
    """Find perimeter of the circle
    
    Args:
        r: Radius of the circle

    Returns:
        Perimeter of the circle
    """
    return 2 * math.pi * r

