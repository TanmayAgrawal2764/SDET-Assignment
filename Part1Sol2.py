import Part1,pytest

#Here the name must start with the prefix "test", otherwise not considered the part of testing.
def test_is_prime():
    assert Part1.is_prime(4)==False#check for first positive non-prime number
    assert Part1.is_prime(2)==True#check for first prime number
    assert Part1.is_prime(3)==True#check for first odd prime number
    assert Part1.is_prime(1)==False#check for invalid prime number
    assert Part1.is_prime(-1)==False#check for negative number
    assert Part1.is_prime(0)==False#check for zero/invalid number
    assert Part1.is_prime(13)==True#check for normal random number
    assert Part1.is_prime(100000000)==False#check for large number


def test_calculate_discount():
    assert Part1.calculate_discount(100,10)==90#case for normal discount
    assert Part1.calculate_discount(100,0)==100#case for zero discount
    assert Part1.calculate_discount(100,100)==0#case for full discount
    assert Part1.calculate_discount(1000000,10)==900000#case for high price
    with pytest.raises(ValueError, match="Price and discount should be numbers."):
        Part1.calculate_discount("100", 10)

    with pytest.raises(ValueError, match="Price and discount should be numbers."):
        Part1.calculate_discount(100, "10")

    with pytest.raises(ValueError, match="Price and discount should not be negative."):
        Part1.calculate_discount(-100, 10)

    with pytest.raises(ValueError, match="Price and discount should not be negative."):
        Part1.calculate_discount(100, -10)

    with pytest.raises(ValueError, match="Discount cannot be more than 100%."):
        Part1.calculate_discount(100, 110)