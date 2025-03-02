import allure
import pytest
import requests

@allure.title("Verify GET Method for restful booker and status should be 200")
@allure.description("This testcase is to verify get request gives the response with status code 200")
@pytest.mark.positive
def test_get_booking_positive():
    print("POSITIVE GET SCENARIO")
    my_url= 'https://restful-booker.herokuapp.com/booking'
    response_data= requests.get(url=my_url)
    assert response_data.status_code==200    #assertion is a statement


@allure.title("Verify GET Method with invalid booking ID")
@allure.description("This testcase is to verify get request gives the response with status code 404")
@pytest.mark.negative
def test_get_booking_negative():
    print("Negative 'GET booking by ID' SCENARIO")
    my_url= 'https://restful-booker.herokuapp.com/booking/-1'
    response_data= requests.get(url=my_url)
    assert response_data.status_code==404   #assertion is a statement