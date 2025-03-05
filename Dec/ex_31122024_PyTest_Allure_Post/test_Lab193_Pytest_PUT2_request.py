import pytest
import allure
import requests

from Dec.ex_31122024_PyTest_Allure_Post.test_Lab192_Pytest_CreateToken import full_url

#Created put request using GetbookingIDbyName URL.
#It worked fine. If in future the code doesnt work
#first create a new booking (using Lab191) with the
# firstname and lastname payload used here and then run this put request

base_url="https://restful-booker.herokuapp.com"
auth_path="/auth"
book_path="/booking?firstname=Anshu&lastname=Priya"
token_url=base_url+auth_path
full_url= base_url+ book_path
headers={
    "Content-Type":"application/json"
}


def create_token():
    valid_payload={
    "username" : "admin",
    "password" : "password123"
}
    response_data=requests.post(url=token_url,headers=headers,json=valid_payload)
    print(response_data.text)
    res_json=response_data.json()
    token=res_json['token']
    print(token)
    return token

def get_bookingid():

    response_data_book= requests.get(url=full_url, headers=headers)
    book_json= response_data_book.json()
    id=book_json[0]["bookingid"]
    print(id)
    return id


def test_put_request():
    token= create_token()
    id=get_bookingid()
    #print(token)
    #print(id)

    put_url= base_url+ "/booking/"+str(id)
    put_payload= {
    "firstname": "Anshu",
    "lastname": "Singh",
    "totalprice": 500,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2025-01-01",
        "checkout": "2026-01-01"
    },
    "additionalneeds": "Garden"
}

    cookie="token="+token
    headers1={
        "Content-Type":"application/json",
        "Cookie":cookie
    }
    res_put= requests.put(url=put_url, headers=headers1, json=put_payload)
    assert res_put.status_code== 200
    res_put_json= res_put.json()
    assert res_put_json['lastname']== "Singh"



def test_delete():
    token= create_token()
    id= get_bookingid()
    url=base_url+"/booking/"+str(id)
    cookie = "token=" + token
    headers2 = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }

    res_delete= requests.delete(url=url,headers=headers2)
    assert res_delete.status_code== 201


