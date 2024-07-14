Assalomu alaykum ustoz. Codni commit qilib bo'lib, jo'natgandan keyin sezib qoldim, ikkinchi password(database dan kelayotgan) passwordni gensalt ham, 
bcrypt.hashpw() ham qilinmas ekan. Shunda cod to'g'ri ishlaydi, lekin bu changeni commit qilmadim, chunki noqonuniy.
Mana Xudo xohlasa, aniq ishlaydigan kod:
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
        if bcrypt.checkpw(user_bytes,hash):
            print("Password match!")
        else:
            print("Passwords do not match.")
    else:
        print("User not found.")

hash_match_password()
