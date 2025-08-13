#override the __len__() method on vector of problem 5 to display the dimension of the vector 

class Vector:
    def __init__(self, values):
        self.values = values

    def __add__(self, other):
        result = [a + b for a, b in zip(self.values, other.values)]
        return Vector(result)

    def __mul__(self, other):
        return sum(a * b for a, b in zip(self.values, other.values))

    def __str__(self):
        if len(self.values) != 3:
            return str(self.values)
        return f"{self.values[0]}i + {self.values[1]}j + {self.values[2]}k"

    def __len__(self):
        return len(self.values)

# Example usage
v = Vector([7, 8, 10])
print("Vector:", v)        # 7i + 8j + 10k
print("Dimension:", len(v))  # 3
