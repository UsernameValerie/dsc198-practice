from twosum import twosum
 
 
def test_pair_at_the_start():
    assert twosum([2, 7, 11, 15], 9) == [0, 1]
 
 
def test_no_pair_exists():
    assert twosum([1, 2, 3], 100) == []

def test_no_loop():
    assert twosum([], 5) == []

def test_duplicate():
    assert twosum([3, 3], 6) == [0, 1]

