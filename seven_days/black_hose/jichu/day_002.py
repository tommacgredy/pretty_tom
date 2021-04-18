import xlrd


class Person:


    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return  "我的名字叫%s，体重是%.2f公斤" % (self.name, self.weight)

    def runing(self):
        print("%s爱跑步，跑步锻炼身体" % self.name)
        self.weight -= 0.5

    def eatting(self):
        print("%s 爱吃饭，吃饭长胖" % self.name)
        self.weight += 1


class HouseItem:

    def __init__(self, name, area):

        self.name = name
        self.area = area

    def __str__(self):

        return "%s 占地面积是 %.2f" % (self.name, self.area)


class House:

    def __init__(self, house_type, area):

        self.house_type = house_type
        self.area = area
        # 剩余面积
        self.free_area = area
        # 家具列表
        self.item_list = []

    def __str__(self):

        return ("房子: %s\n面积: %.2f[剩余面积：%.2f]\n家具列表：%s" %
                (self.house_type, self.area, self.free_area, self.item_list))

    def add_item(self, item):

        print("需要添加的家具：%s" % item)
        # 判断家具大小
        if item.area > self.free_area:
            print("%s 面积过大,放不下" % item.name)

            return

        # 能放下，在item_list中增加家具名称
        self.item_list.append(item.name)

        # 放置家具之后，剩余面积将减少
        self.free_area -= item.area


# bad = HouseItem("床子", 4)
# guizi = HouseItem("柜子", 2)
# desk = HouseItem("桌子", 1)
#
# print(bad)
#
# my_house = House("两室一厅", 75)
# my_house.add_item(bad)
# my_house.add_item(guizi)
# my_house.add_item(desk)
# print(my_house)


# 继承（派生                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               ）的语法 class 类名（父类）
class Anamal:

    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")

class Dog(Anamal):

    def bark(self):
        print("叫")


class Game(object):

    # 历史最高分(类属性)
    top_score = 0

    # 玩家姓名
    def __init__(self, player_name):
        self.player_name = player_name

    # 游戏帮助(静态方法)
    @staticmethod
    def show_help():
        print("帮助文档")

    # 游戏历史记录（类方法）
    @classmethod
    def show_top_scores(cls):
        print("历史记录 %d" % cls.top_score)

    # 开始游戏（对象方法）
    def start_game(self):
        print("%s 开始游戏" % self.player_name)


# # 查看帮助信息
# Game.show_help()
#
# # 查看历史最高分
# Game.show_top_scores()
#
# # 创建游戏对象
# game = Game("小明")
# game.start_game()

class MusicPlayer(object):

    def __init__(self):

        print("音乐播放器初始化")

    def __new__(cls, *args, **kwargs):

        print("分配内存空间")
        obvalue = super().__new__(cls)
        return obvalue

# player = MusicPlayer()
# print(player)


def read_data():
    book = xlrd.open_workbook(r'C:\Users\Administrator\Desktop\data_info.xlsx', 'r')  # 读取data_info表格中的内容
    table = book.sheet_by_index(0)   # 读取第一个sheet页
    new_row = [table.row_values(rowvalue, 0, table.ncols) for rowvalue in range(1, table.nrows)]
    return new_row

def read_xpath_data(xpath_name):
    book = xlrd.open_workbook(r'C:\Users\Administrator\Desktop\data_xpath.xlsx', 'r')  # 读取data_xpath表格中的内容
    table = book.sheet_by_index(0)   # 读取第一个sheet页
    print(table.row(1)[0].value)
    for rowvalue in range(1, table.nrows):
        if table.row(rowvalue)[0].value == xpath_name:
            return table.row(rowvalue)[1].value


a = read_data()
print(a)

b = read_xpath_data('passwd_xpath')
print(b)


