#coding=utf-8
import requests


# 设置url
url = "http://api.nnzhp.cn/api/user/stu_info"

# 请求的参数
myparam = {
    'stu_name' : 'hujintao'
}

# 发送请求
response = requests.get(url, params=myparam)

# 获取响应数据
# -----响应行------
print("url:", response.url)
print("响应码状态：", response.status_code)
# -----响应头------
print("获取响应头：", response.headers)
print("获取指定的响应头：", response.headers.get("Content-Type"))
print("编码集：", response.encoding)
print("获取cookie：", response.cookies)
# -----响应体------
print("文本方式显示响应体：", response.text)
print("二进制方式显示响应体：",response.content) # 主要获取图片或者音频、视频文件

# 转化为json格式之后可以调用json解析函数，如果响应体不能转化成json格式，则会报错
print("将响应体解析为json格式：", response.json().get("results"))
