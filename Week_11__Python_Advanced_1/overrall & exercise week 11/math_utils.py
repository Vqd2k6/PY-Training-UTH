from math import gcd as math_gcd 

def is_prime(n: int) -> bool:
    """Kiểm tra số nguyên tố."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def gcd(a: int, b: int) -> int:
    """Tính Ước chung lớn nhất."""
    return math_gcd(a, b)

def lcm(a: int, b: int) -> int:
    """Tính Bội chung nhỏ nhất."""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)


if __name__ == '__main__':
    
    print(f"is_prime(17) = {is_prime(17)}") # True
    print(f"is_prime(18) = {is_prime(18)}") # False
    
    print(f"gcd(48, 18) = {gcd(48, 18)}") # 6
    
    print(f"lcm(48, 18) = {lcm(48, 18)}") # 144