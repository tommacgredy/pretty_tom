#coding=utf-8
import requests

"""
需求：
以管理员身份登录牛牛网，为用户充值金币
需要先获取cookie值，然后再充值
"""

# 查询接口
url_search = "http://api.nnzhp.cn/api/user/stu_info"
myparams_01 = {
    "stu_name" : "jiangzemin"
}

# 查询用户，获取用户ID
response_search = requests.get(url_search, params=myparams_01)
usr_id = response_search.json().get("stu_info")[0].get("id")
print(usr_id)



# 登录接口，以及管理员账号信息
url_login = "http://api.nnzhp.cn/api/user/login"
myparams_02 = {
    "username" : "niuhanyang",
    "passwd" : "aA123456"
}

# 登录管理员账号
response_login = requests.post(url_login, data=myparams_02)

print("响应状态码：", response_login.status_code)
print("响应头：", response_login.headers)
print("响应体：", response_login.text)
print("cookeie：", response_login.cookies)


# 充值接口，以及所需要的数据
url_addgold = "http://api.nnzhp.cn/api/user/gold_add"
myparams_03 = {
    "stu_id" : usr_id,
    "gold" : 2078522
}

# 获取cookie值
cookie_value = response_login.json().get("login_info").get("sign")
cookie = {
    "niuhanyang" : cookie_value
}

# 为用户充值
response_add = requests.post(url_addgold, data=myparams_03, cookies=cookie)
print("响应状态码：", response_add.status_code)
print("响应体：", response_add.text)
