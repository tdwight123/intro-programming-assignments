"""
Tim Dwight
Sanel
CS1210
LAB 4
"""

def num_to_digits(n):
    return (n // 100 % 100, (n // 10) % 10, (n % 10))

if __name__ == '__main__':
    print(num_to_digits(0))
    print(num_to_digits(50))
    print(num_to_digits(250))