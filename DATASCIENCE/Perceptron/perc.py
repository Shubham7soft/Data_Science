def step(x):
    return 1 if x >= 0 else 0

def perceptron(x1, x2, w1, w2, b):
    y = w1 * x1 + w2 * x2 + b
    return step(y)

print(perceptron(1, 2, 0.5, -0.5, -0.5))  # Example usage
print(perceptron(2, 3, 0.5, -0.5, -0.5))  # Example usage with different inputs
print(perceptron(0, 0, 0.5, -0.5, -0.5))  # Example usage with zero inputs
print(perceptron(1, 1, 0.5, -0.5, -0.5))  # Example usage with equal inputs