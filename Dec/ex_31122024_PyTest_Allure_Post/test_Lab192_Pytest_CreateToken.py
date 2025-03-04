import pytest
import allure
import requests

#Working on Post Request to create token

base_url="https://restful-booker.herokuapp.com"
base_path="/auth"
full_url=base_url+base_path
headers={
    "Content-Type":"application/json"
}

@allure.title("TC001 Create Token_Valid")
@allure.description("Valid Token")
@pytest.mark.token
def test_create_token():
    valid_payload={
    "username" : "admin",
    "password" : "password123"
}
    response_data=requests.post(url=full_url,headers=headers,json=valid_payload)
    print(response_data.text)
    res_json=response_data.json()
    token=res_json['token']
    print(token)
    assert type(token)== str
    assert len(token) == 15

