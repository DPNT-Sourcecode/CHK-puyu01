def compute(x, y):
    def sum(a, b):
        if 0 <= a <= 100 and 0 <= b <= 100:
            return a + b
        else:
            raise ValueError("Both parameters must be between 0 and 100")
    
    return sum(x, y)

