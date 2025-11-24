def add(a, b):
    return a + b

# Tests
def test_add_positive_numbers():
    assert add(int("2"), int("3")) == 5
    
def test_add_negative_numbers():
    assert add(int("-4"), int("-6")) == -10
    
def test_add_zero():
    assert add(int("0"), int("5")) == 5
