from typing import List, Dict, Optional 

def add(x1: float, x2: float) -> Optional[float]:
    if not x1 or not x2:
        return None
    else:
        return x1 + x2

def subtract(x1: float, x2: float) -> Optional[float]:
    if not x1 or not x2:
        return None
    else:
        return x1 - x2
