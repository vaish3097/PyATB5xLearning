def method1():
    print("This is not a pytest testcase method")

def test_method2():
    print("This is pytest testcase method")
    assert True==False    #assertion is a statement