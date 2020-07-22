import json
import requests
import config

def main():
    email = config.EMAIL
    password = config.PASSWORD
    api_key = config.APIKEY

    ret_json = sign_in_with_email_and_password(api_key, email, password)

    print(json.dumps(ret_json, indent=2))

def sign_in_with_email_and_password(api_key, email, password):
    uri = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key={}".format(api_key)
    data = {"email": email, "password": password, "returnSecureToken": True}

    result = requests.post(url=uri, data=data)
    print(result)

    return result.json()

if __name__ == '__main__':
    main()
