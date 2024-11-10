import bcrypt 

def create_account():
    print('Create Account')
    username = input('Enter username: ')
    password = input('Enter password: ')

    # generating the salt 
    salt = bcrypt.gensalt() 

    # Hashing the password 
    hash = bcrypt.hashpw(password.encode('utf-8'), salt) 

    print('Your account has been created successfully')

    return username, hash


def login(username, hash):
    print('Login now')
    username_login = input('Enter username: ')
    password_login = input('Enter password: ')

    if username == username_login and bcrypt.checkpw(password_login.encode('utf-8'), hash):
        print('You\'re logged in sucessfully')

    else:
        print("Invalid credentials!")

def main():
    username, hash = create_account()

    login(username, hash)

# we'll later cover the python modules 
if __name__ == '__main__':
    main()


