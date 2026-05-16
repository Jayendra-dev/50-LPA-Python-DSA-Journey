def is_prime_optimized(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:  # Even number 2 ke alawa prime nahi
        return False
    
    # Sirf sqrt(num) tak check karo, odd numbers se
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    
    return True

# Test karo  
print(is_prime_optimized(29))  # True
print(is_prime_optimized(100)) # False
