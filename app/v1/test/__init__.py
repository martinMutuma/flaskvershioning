#app/v1/test/__init__.py

from app import app
import json
client = app.test_client()



def signup(sign_up_Data = ""):
    """ user signup function """

    if not sign_up_Data:
        sign_up_Data = TestData.user_signup_data
        client.post()
    response = client.post(
        "/api/v1/auth/signup",
        data=dict(sign_up_Data)
    )
    print(str(response))
    return response

class TestData:
    user_signup_data = {
        'username':"Mutuma w34",
        'email':'adminw@admin.com',
        'password':'passWord'
          }