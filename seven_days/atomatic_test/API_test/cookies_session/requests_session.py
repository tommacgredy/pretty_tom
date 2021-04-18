#coding=utf-8
import requests


session = requests.Session()

"""
# 查询接口
url_search = "http://api.nnzhp.cn/api/user/stu_info"
myparams_01 = {
    "stu_name" : "jiangzemin"
}

# 查询用户名，获取用户id
response_search = session.get(url_search, params=myparams_01)
usr_id = response_search.json().get("stu_info")[0].get("id")
print(usr_id)


# 登录接口，以及管理员账号信息
url_login = "http://api.nnzhp.cn/api/user/login"
myparams_02 = {
    "username" : "niuhanyang",
    "passwd" : "aA123456"
}

# 登录
response_login = session.post(url_login, data=myparams_02)
print("响应体：", response_login.text)


# 充值接口，以及所需要的数据
url_addgold = "http://api.nnzhp.cn/api/user/gold_add"
myparams_03 = {
    "stu_id" : usr_id,
    "gold" : 2078522
}

# 充值
response_add = session.post(url_addgold, data=myparams_03)
print("响应体：", response_add.text)

"""
import re

url_01 = "http://192.168.0.8:8080/oa/login.jsp"
mydata_01 = {
    "loginId" : "fuc",
    "password" : "f1234567"
}
response_001 = requests.post(url_01, data=mydata_01)
print("响应体：", response_001.text)
print("响应头：", response_001.headers)

cookie_value02 = response_001.headers.get("Set-Cookie")
cookie_value03 = re.search("JSESSIONID=(.*?);", cookie_value02)
print(cookie_value03.group()[11:-1])
cookies_02 = {
    "JSESSIONID" : cookie_value03.group()[11:-1],

}

form_header = {
    "User-Agent" : "Chrome/86.0.4240.183",
    "Host" : "192.168.0.8:8080"
}

# url_02 = "http://192.168.0.8:8080/oa/jsp/collaborate/approve/sended/list.jsp"
# mydata_02 = {
#     "searchCondition" : "subject",
#     "subject" : "第",
#     "queryType" : "SEARCH",
#     "secretLevel" : 271,
#     "urgentLevel" : 269,
#     "countperpage" : 50,
#     "pageno" : 1
# }
#
# response_002 = requests.post(url_02, data=mydata_02, cookies=cookies_02)
# print(response_002.text)
# print(response_002.status_code)

url_03 ="http://192.168.0.8:8080/oa/jsp/collaborate/approve/sended/index.jsp"
response_003 = requests.get(url_03, headers=form_header, cookies=cookies_02)
print(response_003.text)