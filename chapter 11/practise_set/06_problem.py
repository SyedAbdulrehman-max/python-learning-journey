#write _str_() method to print the vector as follows:
# 7i + 8j +10k
#assume vector of dimension 3 for this proclass Vector:

class Vector:
    def __init__(self, values):
        if len(values) != 3:
            raise ValueError("Only 3D vectors are supported for this format")
        self.values = values

    def __add__(self, other):
        result = [a + b for a, b in zip(self.values, other.values)]
        return Vector(result)

    def __mul__(self, other):
        return sum(a * b for a, b in zip(self.values, other.values))

    def __str__(self):
        return f"{self.values[0]}i + {self.values[1]}j + {self.values[2]}k"

# Example usage
v1 = Vector([7, 8, 10])
print("Vector:", v1)  # Output: 7i + 8j + 10k
