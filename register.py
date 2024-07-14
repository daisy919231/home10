from session import Session
from db import cursor, conn, commit
from models import UserRole, UserStatus, User

session = Session()

@commit
def register():
    while True:
        username = input('Please enter a username: ')
        

        get_user_by_username = 'SELECT * FROM users WHERE username = %s;'
        cursor.execute(get_user_by_username, (username,))
        user_data = cursor.fetchone()

        if user_data:
            print('The username already exists. Please try a different username.')
        else:
            password = input('Please enter a password: ')
            role = input('Please choose a role: User or Admin: ')
            insert_user_query = """
            INSERT INTO users (username, password, role, status, login_try_count)
            VALUES (%s, %s, %s, %s, %s);
            """
            user_status = 'ACTIVE'
            login_try_count = 0
            user_data = (username, password, role, user_status, login_try_count)
            cursor.execute(insert_user_query, user_data)
            session.add_session()
            break  
register()