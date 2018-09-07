import login

def getToken(user_name='17727820013', password='123456'):
    try:
        return login.login(login_num=user_name, password=password)['data']['token']
    except Exception as err:
        print(err)

if __name__ == '__main__':
    print(getToken())
        
    

