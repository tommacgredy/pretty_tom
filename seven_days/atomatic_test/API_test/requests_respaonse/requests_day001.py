#coding=utf-8
import requests


# 设置资源路径、url、请求参数
# get请求发送参数时是以键值对的形式发送请求的，因此参数需要配置成字典的形式
url_01 = "http://api.nnzhp.cn/api/user/stu_info"
myparam = {
    'stu_name' : 'hujintao',
}

# 发送请求（获取学生信息）
response_01 = requests.get(url_01, params=myparam)


# 获取响应状态码、响应体
print("返回的响应状态码为：", response_01.status_code)
print("返回的响应体为：", response_01.text)


# post请求(增加学生信息的接口)
url_02 = 'http://api.nnzhp.cn/api/user/add_stu'

# 提交处理的数据
myjson = {
            "name":"hujintao",
            "grade":"双鱼座",
            "phone":"18688996600",
            "sex":"男",
            "gold":1078522
}

# 查看响应结果
response_02 = requests.post(url_02, json=myjson)

print("相应状态码：", response_02.status_code)
print("响应体：", response_02.text)