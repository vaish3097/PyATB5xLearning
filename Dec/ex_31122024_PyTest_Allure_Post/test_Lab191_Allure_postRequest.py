import pytest
import allure
import requests

#Working on Post Request to create a booking
base_url= 'https://restful-booker.herokuapp.com'
base_path='/booking'
full_url=base_url+base_path;

headers={
        "Content-Type": "application/json"
}

@allure.title("TC001 Verify to create a new booking")
@allure.description("Creating a new booking-Positive sceanrio ")
@pytest.mark.crud
def test_create_booking_positive_tc1():

    payload= {
    "firstname" : "Toshi",
    "lastname" : "Singh",
    "totalprice" : 500,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2025-01-01",
        "checkout" : "2026-01-01"
        },
    "additionalneeds" : "Breakfast"
    }

    response_data= requests.post(url=full_url, headers=headers, json=payload)
    assert response_data.status_code==200
    res_json= response_data.json()

    # checks for bookingid
    booking_id=res_json['bookingid']
    assert booking_id is not None
    assert booking_id >0
    assert type(booking_id) == int

    # checks for firstname, similarly like below we can do checks for lastname, checkin and checkout
    firstname= res_json['booking']['firstname']
    assert firstname == 'Toshi'
    assert type(firstname) == str

    # checks for response time
    res_time=response_data.elapsed.total_seconds()
    assert res_time <1000


@allure.title("TC002 Verify to create a new booking with invalid payload")
@allure.description("No booking will be created with invalid payload-Negative scenario ")
@pytest.mark.crud
def test_create_booking_negative_tc2():
    payload1={}
    response_data_neg= requests.post(url=full_url, headers=headers, json=payload1)
    #res_json1= response_data_neg.json()
    assert response_data_neg.status_code == 500
    print(response_data_neg.text)