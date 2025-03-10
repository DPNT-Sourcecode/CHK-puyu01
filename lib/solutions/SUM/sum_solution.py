def compute(x, y):
    def sum(a, b):
        print(f"Received parameters: a={a}, b={b}")  # Debugging line
        if 0 <= a <= 100 and 0 <= b <= 100:
            result = a + b
            print(f"Sum result: {result}")  # Debugging line
            return result
        else:
            raise ValueError("Both parameters must be between 0 and 100")
    
    return sum(x, y)
