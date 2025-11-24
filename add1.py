import sys

def add(a, b):
    return a + b

if _name_ == "_main_":
    if len(sys.argv) != 3:
        print("Usage: python script.py <num1> <num2>")
        sys.exit(1)
    
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    print("Sum:", add(x, y))
