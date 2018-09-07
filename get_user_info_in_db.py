from utils import mydb


def getUserInfoInDB(user_nickname="手机商家"):
    """
    函数名：getUserInfoInDB
    函数功能：在数据库中获取某个用户的各种信息
    输入参数：
    user_nickname---用户的昵称，如果是非商家用户则为手机或者邮箱号，如果是商家则是商家昵称
    输出参数：返回一个字典，通过键来访问
    user_id---唯一标志用户的字段
    login_times---登录次数统计，目前暂时无法实现
    reg_device---注册的设备，1PC,2安卓，3IOS，4H5
    verify_identity_status---身份认证状态，1身份已认证，2身份未认证
    Verify_tel_status---绑定手机状态，返回Y或者N
    Verify_email_status---绑定邮箱状态，返回Y或者N
    Verify_Google_status---开启谷歌二次认证，Y或者N
    set_account_pwd_status---是否设置资金密码，Y或者N
    reg_time---注册时间，返回datetime.datetime()格式的，也许需要转换才能使用
    my_invite_code---当前用户的邀请码
    inviter_code---邀请该用户的用户邀请码，如果没有返回None
    first_deal_status---是否进行首次交易，1则不是首次交易，2是没有进行首次交易
    fiat_unit---法币切换，目前这字段暂时不使用
    """
    try:
        db = mydb.MyDB()

        user_sql = """SELECT * 
                      FROM User 
                      WHERE nikeName = {0};""".format(repr(user_nickname))
        user_info_dict = db.fetch_data_from_db(user_sql)[0]
        
        return dict(
                    user_id=user_info_dict['userId'],
                    login_times=user_info_dict['loginCount'],
                    reg_device=user_info_dict['regDev'],
                    verify_identity_status=user_info_dict['isVerifyIdentity'],
                    Verify_tel_status=user_info_dict['isVerifyTel'],
                    Verify_email_status=user_info_dict['isVerifyEmail'],
                    Verify_Google_status=user_info_dict['isVerifyGoogle'],
                    set_account_pwd_status=user_info_dict['isSetAcc'],
                    reg_time=user_info_dict['regtime'],
                    my_invite_code=user_info_dict['myInviteCode'],
                    inviter_code=user_info_dict['inviterCode'],
                    first_deal_status=user_info_dict['isFirst'],
                    fiat_unit=user_info_dict['fiatUnit']
                   )
    except Exception as err:
        print(err)
    else:
        pass
    finally:
        db.close_db()

if __name__ == '__main__':
    print(getUserInfoInDB.__doc__)
    for i, j in getUserInfoInDB().items():
        print(i, '==>', j)
