import pytest
@pytest.mark.parametrize("x", [-1, 0, 1], ids=["negative", "zero", "positive"])
@pytest.mark.parametrize("y", [100, 1000], ids=["3 digit", "4 digit"])
def test_multiply_params(x, y):
   print("x: {0}, y: {1}".format(x, y))
   assert True