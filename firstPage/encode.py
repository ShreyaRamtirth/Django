import datetime
import jwt
SECRET_KEY = "python_jwt"

def encode_data_values(data):
    json_data = {
        "Username": data['email'],
        "password": data['password'],
        "date": str(datetime.datetime.now())
    }
    encode_data = jwt.encode(payload=json_data, \
                            key=SECRET_KEY, algorithm="HS256")
    print(encode_data)