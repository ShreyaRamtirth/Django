import datetime
import jwt
SECRET_KEY = "python_jwt"

def encode_data_values(data):
    json_data = {
        "Username": data['email'],
        "Name": data['name'],
        "role": data['role'],
        "date": str(datetime.datetime.now())
    }
    encode_data = jwt.encode(payload=json_data, \
                            key=SECRET_KEY, algorithm="HS256")
    return encode_data