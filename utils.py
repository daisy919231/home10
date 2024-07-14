from db import conn,cursor,commit
import bcrypt
from models import User
class Response:
    def __init__(self, data: str, status_code: int):
        self.data = data
        self.status_code = status_code


def hash_match_password():
    username = input('Please enter your username: ')
    raw_password = input('Please enter your password:  ')
    bytes = raw_password.encode('utf-8')
    salt=bcrypt.gensalt()
    hash=bcrypt.hashpw(bytes,salt)

    get_user_by_username = '''
    SELECT * FROM users WHERE username = %s;
    '''
    cursor.execute(get_user_by_username, (username,))
    user_data = cursor.fetchone()

    if user_data:
        encoded_password = user_data[2]
        user_bytes = encoded_password.encode('utf-8')
        salt2=bcrypt.gensalt()
        hash2=bcrypt.hashpw(user_bytes,salt)
        if bcrypt.checkpw(hash, hash2):
            print("Password match!")
        else:
            print("Password does not match.")
    else:
        print("User not found.")

hash_match_password()