#coding=utf-8

"""
str_01 = "hello World"
str_02 = "123456"

# 字符串连接
# 使用“+”
str_03 = str_01 + str_02
print(str_03)
# 使用jion方法，以 str_01 作为分隔符，将str_02中所有的元素(的字符串表示)合并为一个新的字符串
str_04 = str_01.join(str_02)
print(str_04)

# 字符串切片（根据索引值切片）
print(str_01[1:])  # 获取索引值1之后的所有字符
print(str_02[1:4])  # 获取索引值1-4之间的字符
print(str_03[1:6:2])  # 获取索引值1-6之间的字符，每隔两个取一个值
print(str_04[::-1])  # 将字符串倒序排列
print(str_01[:4:2])  # 获取索引值0-4之间的字符，每隔两个取一个值

# 字符串常用的方法
print(str_01.upper())  # 将字符串全部转化成英文大写
print(str_01.lower())  # 将字符串全部转化成英文小写
print(str_01.strip())  # 去除字符串中的所有空格
print(str_01.capitalize())  # 将字符串中的首字母大写

str_05 = "my name is {}"
print(str_05.format("Jhon"))  # 格式化输出
print(str_05.count("m"))  # 统计字符串中某一个元素的出现的次数
print(str_05.replace("my", "My"))  # 替换字符串中的某一个元素
print(len(str_05))  # 统计字符串的长度
print(str_05.split(" "))  # 将字符串以空格进行切片，结果以列表的形式输出

list_01 = [1, 3, "xuehua", "124"]

list_01.append("abf")  #在列表末尾添加新的对象
list_01.count(1)  # 统计某个元素在列表中出现的次数
list_01.extend([3, 2, "jianpan"])  # 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
list_01.index("xuehua")  # 从列表中找出某个值第一个匹配项的索引位置,index(指定元素,start,end)，start、end 表示从哪个位置开始进行搜索
list_01.insert(2, "haha")  # 将对象插入列表
list_01.pop(-1)  # 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
list_01.remove(3)  # 移除列表中某个值的第一个匹配项
list_01.reverse()  # 反向列表中元素
list_01.sort()  # 对原列表进行排序,默认升序
list_01.clear()  # 将列表中的元素全部清除


def func(list_01):
    for i in list_01[:]:
        if list_01.count(i) > 1:
            list_01.remove(i)

    print(len(list_01))


def func_01(list_02):
    for i in list_02:
        n = list_02.count(i)

        if n > 1:
            for j in range(1,n):
                list_02.remove(i)


# 字典的用法
# 1.字典的创建
# 直接创建
dic_01 = {"name" : "tom", "age" : "18", "gender" : "Male"}
print(dic_01)
print(dic_01["name"])  # 通过键获取字典中的值，若键不存在则会报错

# 使用zip函数创建
key_01 = ["name", "age", "gender"]
value_01 = ["jack", 32, "Male"]
dic_02 = dict(zip(key_01, value_01))
print(dic_02)

# 2.字典常用的方法
# 获取字典中的值，用get()方法，若键不存在，不会报错，输出None
print(dic_02.get("name"))

if dic_02.get("job") == None:
    print("失业")

# 获取所有的键值对
print(dic_01.items())
# 输出：dict_items([('name', 'tom'), ('age', '18'), ('gender', 'Male')])

# 遍历所有的键值对
for i in dic_01.items():
    print(i)
    # 输出：('name', 'tom')  ('age', '18')  ('gender', 'Male')

# 获取字典中的键
print(dic_01.keys())  # dict_keys(['name', 'age', 'gender'])
print(type(dic_01.keys()))  # <class 'dict_keys'>

# 获取字典中的值
print(dic_01.values())  # dict_values(['tom', '18', 'Male'])

# 字典中的键值对的个数
print(len(dic_02))  # 3

# 向字典中增加元素，如果新增的键不存在，则创建新的键和值，如果键存在，则更新键所对应的值
dic_02["name"] = "john"
print(dic_02["name"])
dic_02["job"] = "tester"
print(dic_02)  # 输出：{'name': 'john', 'age': 32, 'gender': 'Male', 'job': 'tester'}

# 使用update方法，将b字典合并到a字典中，如果键存在，则将a字典中的值覆盖，如果不存在，则添加到a中
dic_03 = dict([("height", 1.8), ("job", "teacher"), ("weight", 77)])
dic_02.update(dic_03)
print(dic_02)  # {'name': 'john', 'age': 32, 'gender': 'Male', 'job': 'teacher', 'height': 1.8, 'weight': 77}

# 使用del删除元素
del(dic_01["age"])
print(dic_01)  # 输出：{'name': 'tom', 'gender': 'Male'}

# 使用clear方法，清除字典中的所有键值对
dic_02.clear()
print(dic_02)  # 输出：{}

# 使用pop方法，删除键之后，可以使用变量接收返回的值
a = dic_03.pop("height")
print(a)  # 1.8
print(dic_03)  # {'job': 'teacher', 'weight': 77}

# 序列解包
dic_04 = {"name" : "Marry", "age" : 18, "gender" : "Fmale", "job" : "teacher"}
print(dic_04)
b, d, e, f = dic_04.items()
print(b)  # 运行结果：('name', 'Marry')
print(d)  # 运行结果：('age', 18)
print(e)  # 运行结果：('gender', 'Fmale')
print(f)  # 运行结果：('job', 'teacher')
m, n, x, y = dic_04.keys()
print(m)  # 运行结果：name
print(n)  # 运行结果：age



def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print("输出: ")
   print(arg1)
   print(vartuple)
   for var in vartuple:
      print(var)
   return


def f(list_01, d):
    try:
        if isinstance(list_01, list) == True and isinstance(d, int) == True and d >=0:
            if len(list_01) > 1:
                list_02 = [abs(int(list_01[i] - list_01[j])) for i in range(len(list_01)) for j in range(i+1, len(list_01))]
                list_03 = list(set(list_02))
                list_04 = []
                if d in list_03:
                    for i in range(len(list_01)):
                        for j in range(i + 1, len(list_01)):
                            a = abs(int(list_01[i] - list_01[j]))
                            if a == d:
                                list_04.append((list_01[i], list_01[j]))
                else:
                    print("d值不是列表中值的距离！！！")

                list_05 = list(set(list_04))
                for m in list_05:
                    print("{}:{}".format(m[0], m[1]))

                print(len(list_05))
            else:
                print("输入的列表中的值的数目小于两个值")

        else:
            print("输入参数不合法")
    except:
        print("输入参数有误！！！")

"""

import re



def testexchange(teststr):
    print(teststr)
    strsearch = re.search(".*?[,.?!]", teststr)
    it = re.finditer('.*?[,.?!]', teststr)
    resultlist =[]
    for match in it:
        resultlist.append(" ".join(str(match.group())[0:-1].strip().split(" ")[::-1]))
        resultlist.append(str(match.group())[-1] + " ")

    print("".join(resultlist).strip())



def textreverse(str_01):
    str_02 = re.finditer(".*?[,.?!]", str_01)
    list_01 = []
    for i in str_02:
        a = " ".join(i.group()[0: -1].split(" ")[::-1])
        list_01.append(a)
        list_01.append(i.group()[-1])
    print(list_01)
    str_03 = "".join(list_01).strip()
    print(str_03)



def func(list_01, str_01):
    try:
        if isinstance(list_01, list) == True and isinstance(str_01, str) == True:
            if len(list_01) > 0:
                list_02 = []
                for i in list_01:
                    if str(i) in str_01:
                        list_02.append(i)
                m = len(list_02)
                if m > 0:
                    print("True")
                else:
                    print("False")

            else:
                print("False")

        else:
            print("入参类型出错！")
    except:
        print("出现错误！")

if __name__ == "__main__":
    list_02 = ["am","am","am"]
    str_02 = "abcdem"
    func(list_02, str_02)

