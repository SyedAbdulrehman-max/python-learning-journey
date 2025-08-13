'''Type Hints for Collections (Lists, Dicts, etc.)'''

from typing import List, Dict, Tuple, Union, Optional

# List of integers
scores: List[int] = [90, 80, 85]

# Dictionary with string keys and int values
grades: Dict[str, int] = {"Math": 90, "Science": 85}

# Tuple: a string and a float
student: Tuple[str, float] = ("Alice", 5.9)

# Union: value can be int OR string
value: Union[int, str] = "42"

# Optional: value can be int OR None
age: Optional[int] = None

'''
Type Hints for Variables
'''


name: str = "Alice"          # This variable should hold a string
age: int = 25                # Integer value
height: float = 5.7          # Float value
is_student: bool = True      # Boolean (True or False)

# These hints help humans and tools understand your intention

'''
Type Hints in Functions'''

# Function that takes a string and returns a string
def greet(name: str) -> str:
    return f"Hello, {name}"

# Function that adds two numbers
def add(a: int, b: int) -> int:
    return a + b

# You can also skip return types, but it's good practice to include them
