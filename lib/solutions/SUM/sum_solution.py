def sum(a, b):
    # Ensures the parameters are within the specified range
    if a < 0 or a > 100 or b < 0 or b > 100:
        raise ValueError("Parameters must be between 0 and 100")
    return a + b

# Example usage
if __name__ == "__main__":
    print(sum(10, 20))  # Output: 30
