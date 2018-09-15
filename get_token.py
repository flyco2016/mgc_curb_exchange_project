import login

def getToken(user_name='17727820013', password='123456'):
    return login.login(login_num=user_name, password=password)['data']['token']


if __name__ == '__main__':
    print(getToken())
    
        
    

