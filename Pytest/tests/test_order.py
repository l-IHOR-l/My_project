import pytest


@pytest.mark.run(order=2)
def test_method_1():
    print('Method 1')
@pytest.mark.run(order=4)
def test_method_2():
    print('Method 2')
@pytest.mark.run(order=3)
def test_method_3():
    print('Method 3')
@pytest.mark.run(order=1)
def test_method_4():
    print('Method 4')
