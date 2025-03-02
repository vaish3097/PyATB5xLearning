import pytest
def method1():
    print("This is not a pytest testcase method")

@pytest.mark.smoke
def test_method2():
    print("This is pytest testcase method")
    assert True==False    #assertion is a statement

@pytest.mark.regression
def test_method3():
    print("This is another testcase")
    assert 1+1==2