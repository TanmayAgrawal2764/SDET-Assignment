def is_prime(n):
    """Check if a number is a prime number."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def calculate_discount(price, discount):
    """Calculate the price after applying a discount."""
    if not isinstance(price, (int, float)) or not isinstance(discount, (int, float)):
        raise ValueError("Price and discount should be numbers.")
    if price < 0 or discount < 0:
        raise ValueError("Price and discount should not be negative.")
    if discount > 100:
        raise ValueError("Discount cannot be more than 100%.")
    return price - (price * (discount / 100))
