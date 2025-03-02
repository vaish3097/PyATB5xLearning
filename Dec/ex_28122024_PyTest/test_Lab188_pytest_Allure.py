import allure
import pytest


def method1():
    print("This is not a pytest testcase method")

@allure.title("Verify create booking")
@allure.description("testcase is to verify booking id created or not")
@pytest.mark.positive
def test_create_booking_positive():
    print("This is pytest testcase method")
    assert True!=False    #assertion is a statement

@allure.title("Verify create booking- negative scenario")
@allure.description("testcase is to verify booking id created or not")
@pytest.mark.negative
def test_create_negative_booking():
    print("This is another testcase")
    assert 1-1==2