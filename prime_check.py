def is_prime(num):
    # 1 ya usse chhote number prime nahi hote
    if num <= 1:
        return False
    
    # 2 se num-1 tak check karo
    for i in range(2, num):
        if num % i == 0:  # Agar divide ho gaya
            return False  # Prime nahi hai
    
    return True  # Kisi se divide nahi hua = Prime hai

# Test karo
print(is_prime(29))  # True
print(is_prime(10))  # False