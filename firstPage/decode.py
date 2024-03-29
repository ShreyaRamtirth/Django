import jwt
SECRET_KEY = "python_jwt"

def decode_data_values(data):
    token = data
    try:
        decode_data = jwt.decode(jwt=token, \
                                key=SECRET_KEY, algorithms="HS256")
        print(decode_data)
        return decode_data
    except Exception as e:
        message = f"Token is invalid --> {e}"
        print({"message": message})