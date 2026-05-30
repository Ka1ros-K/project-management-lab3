# 登录模块
def login(username, password):
    if username == "admin" and password == "123456":
        return True
    return False

def logout():
    print("已退出登录")
