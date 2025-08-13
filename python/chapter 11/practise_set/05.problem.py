#write a class vector representing a vector of n dimensions. Overload the + and * 
# operator which calculates the sum and the dot(.) product of them
class Vector:
    def __init__(self, values):
        self.values = values

    def __add__(self, other):
        if len(self.values) != len(other.values):
            raise ValueError("Vectors must be of the same length")
        result = [a + b for a, b in zip(self.values, other.values)]
        return Vector(result)

    def __mul__(self, other):
        if len(self.values) != len(other.values):
            raise ValueError("Vectors must be of the same length")
        result = sum(a * b for a, b in zip(self.values, other.values))
        return result

    def __str__(self):
        return str(self.values)

# Example usage
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

print("Sum:", v1 + v2)         # [5, 7, 9]
print("Dot product:", v1 * v2) # 1*4 + 2*5 + 3*6 = 32
